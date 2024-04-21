import pandas as pd
import numpy as np
from darts import TimeSeries
from darts.dataprocessing.transformers import Scaler
from darts.models import TransformerModel
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import logging
from database import connect

# Setting up logging
logging.basicConfig(
    filename='logfilets.log',  
    filemode='a',  
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG 
)

def load_data():
    """ Load data from a CSV file. """
    try:
        client = connect()
        logging.info("MongoDB connection established successfully.")
        db = client.prognostic
        collection = db.healthWorkerData
        cursor = collection.find({})
        data = pd.DataFrame(list(cursor))
        logging.info(data.head())
        logging.debug(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        return None

def clean_data(df, disease):
    """ Clean data by handling missing values and outliers. """
    try:
        df = df[df['Disease'] == disease]
        df['vdate'] = pd.to_datetime(df['vdate'])
        df.set_index('vdate', inplace=True)
        df = df.resample('D').count()
        df['Patients'] = df['Disease']
        df = df[['Patients']]
        logging.debug(f"Data cleaned successfully with")
        return df
    except Exception as e:
        logging.error(f"Failed to clean data: {e}")
        return None

def process_data(df):
    """ Merge two dataframes based on a key. """
    try:
        series = TimeSeries.from_dataframe(df, value_cols='Patients')

        scaler = Scaler()
        series_scaled = scaler.fit_transform(series)

        train, test = series_scaled.split_before(0.9)
        train_val, val = train.split_before(0.6)

        logging.debug(f"Data processed successfully")
        return train, train_val, val, test, series, scaler
    except Exception as e:
        logging.error(f"Failed to merge dataframes: {e}")
        return None

def fit_and_evaluate_model(train, train_val, val, test, series, scaler):
    """ Fit a linear regression model and calculate performance metrics. """
    try:
        model = TransformerModel(
            input_chunk_length=14,  
            output_chunk_length=2,  
            nhead=8,              
            num_encoder_layers=3,   
            num_decoder_layers=3,   
            dim_feedforward=5,    
            dropout=0.2,            
            n_epochs=200,           
            model_name="TransformerModel_GrossAmount"
        )
        model.fit(
            series=train_val,
            val_series=val,
            verbose=1
        )
        forecast = model.predict(n=len(test), series=train)
        forecast_rescaled = scaler.inverse_transform(forecast)
        forecast_df_capped = forecast_rescaled.pd_dataframe().applymap(lambda x: max(x, 0))
        forecast_capped = TimeSeries.from_dataframe(forecast_df_capped)
        forecast_start_date_weekly = test.start_time()
        actual_during_forecast = series.slice(forecast_start_date_weekly, forecast_capped.end_time())

        df1 = forecast_df_capped
        df2 = actual_during_forecast.pd_dataframe()
        df1 = df1.resample('M').sum()
        df2 = df2.resample('M').sum()

        rmse_value = np.sqrt(mean_squared_error(df2['Patients'], df1['Patients']))
        mae_value = mean_absolute_error(df2['Patients'], df1['Patients'])
        r2 = r2_score(df2['Patients'], df1['Patients'])

        mean_actual = np.mean(df2['Patients'])
        normalized_rmse = rmse_value / mean_actual
        normalized_mae = mae_value / mean_actual

        print('RMSE: ',rmse_value)
        print('MAE: ', mae_value)
        print('NRMSE: ', normalized_rmse)
        print('NMAE: ', normalized_mae)
        print('R2-Score: ', r2)

        logging.debug(f"Model fitted and evaluated successfully")
        logging.info(f"RMSE: {rmse_value}, MAE: {mae_value}, NRMSE: {normalized_rmse}, NMAE: {normalized_mae}, R2-Score: {r2}")
        return df1
    except Exception as e:
        logging.error(f"Failed to fit and evaluate model: {e}")
        return None
    
def send_to_mongo(results):
    try:
        client = connect()
        db = client.prognostic
        collection = db.results
        collection.delete_many({})
        results['vdate'] = results.index
        results.reset_index(drop=True, inplace=True)
        collection.insert_many(results.to_dict("records", into=dict))
        logging.info("Data inserted successfully")
    except Exception as e:
        logging.error(f"Failed to send data to MongoDB: {e}")

df = load_data()
df_cleaned = clean_data(df, 'CKD')
train, train_val, val, test, series, scaler = process_data(df_cleaned)
results = fit_and_evaluate_model(train, train_val, val, test, series, scaler)
send_to_mongo(results)