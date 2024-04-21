from pymongo.mongo_client import MongoClient
import pandas as pd

def connect():
    uri = "mongodb+srv://surgicalmasks:6ey0eKacdG2MdmvB@cluster0.uovckvw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)

def intializeData(client):
    # convert csv to json format
    data = pd.read_csv("health_dataset2.csv")

    data.drop(columns=['eid'], inplace=True)
    data.reset_index(drop=True, inplace=True)
    data_dict = data.to_dict("records", into=dict)

    # create a new database
    db = client["prognostic"]
    collection = db["healthWorkerData"]
    
    print("Database created successfully")

    #input the data into the database
    collection.insert_many(data_dict)
    print("Data inserted successfully")
    
def add_csv_data(data, client):
    # check columns are present and return if they are not same
    
    data.drop(columns=['eid'], inplace=True)
    data.reset_index(drop=True, inplace=True)
    data_dict = data.to_dict("records", into=dict)

    collection = client["prognostic"]["healthWorkerData"]

    #input the data into the database
    collection.insert_many(data_dict)
    return "Data inserted successfully"
    
