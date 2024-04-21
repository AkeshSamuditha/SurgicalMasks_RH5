from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from io import StringIO
import pickle
from database import connect, add_csv_data


app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    
class Symptoms(BaseModel):
    rash: bool
    fever: bool
    cough: bool
    sore_throat: bool
    shortness_of_breath: bool
    head_ache: bool
    age: int
    

@app.on_event("startup")
async def startup_event():
    global db
    db = connect()

@app.post("/login")
def login(user: User):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"status": "Logged in"}

@app.post("/symptoms")
def receive_medical_data(data: Symptoms):
    # Process the medical data here
    collection = db.userMedicalData
    collection.insert_one(data.dict())
    
    results = predict_symptoms(data)
    # validated data
    return {"status": "Data received",
            "results": results}

def predict_symptoms(data: Symptoms):
    model = pickle.load(open('model.pkl', 'rb'))
    disease = model.predict(data)

    return disease

'''
input: csv file
output: status message
description: This endpoint is used to receive the medical worker data in the form of a CSV file. The data is then inserted into the MongoDB database.
'''
@app.post("/medical_worker_data")
async def receive_medical_worker_data(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode('utf-8')))
        add_csv_data(df, db)
        return {"status": "Data received"}
    else:
        raise HTTPException(status_code=400, detail="Invalid file type")