import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
import pickle
import logging

# Setting up logging
logging.basicConfig(
    filename='logfilesypmtoms.log',  
    filemode='a',  
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG 
)

def load_data():
    """ Load data from a CSV file. """
    try:
        train_df = pd.read_csv('Training.csv')
        test_df = pd.read_csv('Testing.csv')
        # train_df.columns = range(132)
        # test_df.columns = range(132)
        logging.debug(f"Training data loaded successfully with {train_df.shape[0]} rows and {train_df.shape[1]} columns.")
        logging.debug(f"Testing data loaded successfully with {test_df.shape[0]} rows and {test_df.shape[1]} columns.")
        return train_df, test_df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        return None

def process_data(train_df, test_df):
    """ Merge two dataframes based on a key. """
    try:
        train_x = train_df.iloc[:, :-1]
        train_y = train_df.iloc[:, -1]

        test_x = test_df.iloc[:, :-1]
        test_y = test_df.iloc[:, -1]

        logging.debug(f"Data processed successfully")
        return train_x, train_y, test_x, test_y
    except Exception as e:
        logging.error(f"Failed to merge dataframes: {e}")
        return None

def fit_and_evaluate_model(train_x, train_y, test_x, test_y):
    """ Fit a linear regression model and calculate performance metrics. """
    try:
        model = CatBoostClassifier(iterations=50, learning_rate=0.1, depth=2, loss_function='MultiClass', verbose=False)
        model.fit(train_x, train_y)

        predictions = model.predict(test_x)
        accuracy = accuracy_score(test_y, predictions)
        logging.info(f"Accuracy: {accuracy}")

        pickle.dump(model, open('model.pkl', 'wb'))
        logging.debug(f"Model saved successfully")
        return None
    except Exception as e:
        logging.error(f"Failed to fit and evaluate model: {e}")
        return None

train_df, test_df = load_data()
train_x, train_y, test_x, test_y = process_data(train_df, test_df)
results = fit_and_evaluate_model(train_x, train_y, test_x, test_y)