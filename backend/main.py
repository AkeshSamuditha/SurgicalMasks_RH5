from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from io import StringIO
import pickle
import random
from database import connect, add_csv_data

app = FastAPI()

origins = [
    "https://surgical-masks-rh-5.vercel.app",  # Add your origins here
    "http://localhost:3001",  # Or your local development origin

"https://surgical-masks-rh-5.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class User(BaseModel):
    username: str
    password: str
    
class Symptoms(BaseModel):
    itching: bool
    skin_rash: bool
    nodal_skin_eruptions: bool
    continuous_sneezing: bool
    shivering: bool
    chills: bool
    joint_pain: bool
    stomach_pain: bool
    acidity: bool
    ulcers_on_tongue: bool
    muscle_wasting: bool
    vomiting: bool
    burning_micturition: bool
    spotting_urination: bool
    fatigue: bool
    weight_gain: bool
    anxiety: bool
    cold_hands_and_feets: bool
    mood_swings: bool
    weight_loss: bool
    restlessness: bool
    lethargy: bool
    patches_in_throat: bool
    irregular_sugar_level: bool
    cough: bool
    high_fever: bool
    sunken_eyes: bool
    breathlessness: bool
    sweating: bool
    dehydration: bool
    indigestion: bool
    headache: bool
    yellowish_skin: bool
    dark_urine: bool
    nausea: bool
    loss_of_appetite: bool
    pain_behind_the_eyes: bool
    back_pain: bool
    constipation: bool
    abdominal_pain: bool
    diarrhoea: bool
    mild_fever: bool
    yellow_urine: bool
    yellowing_of_eyes: bool
    acute_liver_failure: bool
    swelling_of_stomach: bool
    swelled_lymph_nodes: bool
    malaise: bool
    blurred_and_distorted_vision: bool
    phlegm: bool
    throat_irritation: bool
    redness_of_eyes: bool
    sinus_pressure: bool
    runny_nose: bool
    congestion: bool
    chest_pain: bool
    weakness_in_limbs: bool
    fast_heart_rate: bool
    pain_during_bowel_movements: bool
    pain_in_anal_region: bool
    bloody_stool: bool
    irritation_in_anus: bool
    neck_pain: bool
    dizziness: bool
    cramps: bool
    bruising: bool
    obesity: bool
    swollen_legs: bool
    swollen_blood_vessels: bool
    puffy_face_and_eyes: bool
    enlarged_thyroid: bool
    brittle_nails: bool
    swollen_extremeties: bool
    excessive_hunger: bool
    extra_marital_contacts: bool
    drying_and_tingling_lips: bool
    slurred_speech: bool
    knee_pain: bool
    hip_joint_pain: bool
    muscle_weakness: bool
    stiff_neck: bool
    swelling_joints: bool
    movement_stiffness: bool
    spinning_movements: bool
    loss_of_balance: bool
    unsteadiness: bool
    weakness_of_one_body_side: bool
    loss_of_smell: bool
    bladder_discomfort: bool
    foul_smell_of_urine: bool
    continuous_feel_of_urine: bool
    passage_of_gases: bool
    internal_itching: bool
    toxic_look_typhos: bool
    depression: bool
    irritability: bool
    muscle_pain: bool
    altered_sensorium: bool
    red_spots_over_body: bool
    belly_pain: bool
    abnormal_menstruation: bool
    dischromic_patches: bool
    watering_from_eyes: bool
    increased_appetite: bool
    polyuria: bool
    family_history: bool
    mucoid_sputum: bool
    rusty_sputum: bool
    lack_of_concentration: bool
    visual_disturbances: bool
    receiving_blood_transfusion: bool
    receiving_unsterile_injections: bool
    coma: bool
    stomach_bleeding: bool
    distention_of_abdomen: bool
    history_of_alcohol_consumption: bool
    fluid_overload: bool
    blood_in_sputum: bool
    prominent_veins_on_calf: bool
    palpitations: bool
    painful_walking: bool
    pus_filled_pimples: bool
    blackheads: bool
    scurring: bool
    skin_peeling: bool
    silver_like_dusting: bool
    small_dents_in_nails: bool
    inflammatory_nails: bool
    blister: bool
    red_sore_around_nose: bool
    yellow_crust_ooze: bool
    prognosis: bool

@app.on_event("startup")
async def startup_event():
    global db
    global SymptomModel
    SymptomModel = pickle.load(open('model.pkl', 'rb'))
    db = connect()

@app.post("/login")
def login(user: User):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"status": "Logged in"}

@app.post("/check")
def check():
    return {"status": "Working"}

@app.post("/symptoms")
def receive_medical_data(data: Symptoms): 
    print(data) 
    results = predict_symptoms(data)
    return {"status": "Data received",
            "results": results}

def predict_symptoms(data: Symptoms):
    dataModel = data.model_dump()
    for key in dataModel:
        dataModel[key] = int(dataModel[key])
    symptoms_instance = pd.DataFrame([dataModel])
    disease = SymptomModel.predict(symptoms_instance)

    # Convert disease to a string representation
    disease_str = str(disease[0][0])

    return disease_str

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