from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from io import StringIO
from database import connect, add_csv_data


app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    
class Symptoms(BaseModel):
    bmi: float
    

@app.on_event("startup")
async def startup_event():
    global client
    client = connect()

@app.post("/login")
def login(user: User):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"status": "Logged in"}

@app.post("/user_data")
def receive_medical_data(data: MedicalData):
    # Process the medical data here
    collection = client["prognostic"]["userMedicalData"]
    collection.insert_one(data.dict())
    return {"status": "Data received"}


@app.post("/medical_worker_data")
async def receive_medical_worker_data(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode('utf-8')))
        
        add_csv_data(df, client)
        return {"status": "Data received"}
    else:
        raise HTTPException(status_code=400, detail="Invalid file type")