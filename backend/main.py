from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from io import StringIO
import pickle
import random
from database import connect, add_csv_data

app = FastAPI()

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
    fluid_overload: bool
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
    fluid_overload1: bool
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

def generate_random_symptoms():
    symptoms = {
        "itching": random.choice([True, False]),
        "skin_rash": random.choice([True, False]),
        "nodal_skin_eruptions": random.choice([True, False]),
        "continuous_sneezing": random.choice([True, False]),
        "shivering": random.choice([True, False]),
        "chills": random.choice([True, False]),
        "joint_pain": random.choice([True, False]),
        "stomach_pain": random.choice([True, False]),
        "acidity": random.choice([True, False]),
        "ulcers_on_tongue": random.choice([True, False]),
        "muscle_wasting": random.choice([True, False]),
        "vomiting": random.choice([True, False]),
        "burning_micturition": random.choice([True, False]),
        "spotting_urination": random.choice([True, False]),
        "fatigue": random.choice([True, False]),
        "weight_gain": random.choice([True, False]),
        "anxiety": random.choice([True, False]),
        "cold_hands_and_feets": random.choice([True, False]),
        "mood_swings": random.choice([True, False]),
        "weight_loss": random.choice([True, False]),
        "restlessness": random.choice([True, False]),
        "lethargy": random.choice([True, False]),
        "patches_in_throat": random.choice([True, False]),
        "irregular_sugar_level": random.choice([True, False]),
        "cough": random.choice([True, False]),
        "high_fever": random.choice([True, False]),
        "sunken_eyes": random.choice([True, False]),
        "breathlessness": random.choice([True, False]),
        "sweating": random.choice([True, False]),
        "dehydration": random.choice([True, False]),
        "indigestion": random.choice([True, False]),
        "headache": random.choice([True, False]),
        "yellowish_skin": random.choice([True, False]),
        "dark_urine": random.choice([True, False]),
        "nausea": random.choice([True, False]),
        "loss_of_appetite": random.choice([True, False]),
        "pain_behind_the_eyes": random.choice([True, False]),
        "back_pain": random.choice([True, False]),
        "constipation": random.choice([True, False]),
        "abdominal_pain": random.choice([True, False]),
        "diarrhoea": random.choice([True, False]),
        "mild_fever": random.choice([True, False]),
        "yellow_urine": random.choice([True, False]),
        "yellowing_of_eyes": random.choice([True, False]),
        "acute_liver_failure": random.choice([True, False]),
        "fluid_overload": random.choice([True, False]),
        "swelling_of_stomach": random.choice([True, False]),
        "swelled_lymph_nodes": random.choice([True, False]),
        "malaise": random.choice([True, False]),
        "blurred_and_distorted_vision": random.choice([True, False]),
        "phlegm": random.choice([True, False]),
        "throat_irritation": random.choice([True, False]),
        "redness_of_eyes": random.choice([True, False]),
        "sinus_pressure": random.choice([True, False]),
        "runny_nose": random.choice([True, False]),
        "congestion": random.choice([True, False]),
        "chest_pain": random.choice([True, False]),
        "weakness_in_limbs": random.choice([True, False]),
        "fast_heart_rate": random.choice([True, False]),
        "pain_during_bowel_movements": random.choice([True, False]),
        "pain_in_anal_region": random.choice([True, False]),
        "bloody_stool": random.choice([True, False]),
        "irritation_in_anus": random.choice([True, False]),
        "neck_pain": random.choice([True, False]),
        "dizziness": random.choice([True, False]),
        "cramps": random.choice([True, False]),
        "bruising": random.choice([True, False]),
        "obesity": random.choice([True, False]),
        "swollen_legs": random.choice([True, False]),
        "swollen_blood_vessels": random.choice([True, False]),
        "puffy_face_and_eyes": random.choice([True, False]),
        "enlarged_thyroid": random.choice([True, False]),
        "brittle_nails": random.choice([True, False]),
        "swollen_extremeties": random.choice([True, False]),
        "excessive_hunger": random.choice([True, False]),
        "extra_marital_contacts": random.choice([True, False]),
        "drying_and_tingling_lips": random.choice([True, False]),
        "slurred_speech": random.choice([True, False]),
        "knee_pain": random.choice([True, False]),
        "hip_joint_pain": random.choice([True, False]),
        "muscle_weakness": random.choice([True, False]),
        "stiff_neck": random.choice([True, False]),
        "swelling_joints": random.choice([True, False]),
        "movement_stiffness": random.choice([True, False]),
        "spinning_movements": random.choice([True, False]),
        "loss_of_balance": random.choice([True, False]),
        "unsteadiness": random.choice([True, False]),
        "weakness_of_one_body_side": random.choice([True, False]),
        "loss_of_smell": random.choice([True, False]),
        "bladder_discomfort": random.choice([True, False]),
        "foul_smell_of_urine": random.choice([True, False]),
        "continuous_feel_of_urine": random.choice([True, False]),
        "passage_of_gases": random.choice([True, False]),
        "internal_itching": random.choice([True, False]),
        "toxic_look_typhos": random.choice([True, False]),
        "depression": random.choice([True, False]),
        "irritability": random.choice([True, False]),
        "muscle_pain": random.choice([True, False]),
        "altered_sensorium": random.choice([True, False]),
        "red_spots_over_body": random.choice([True, False]),
        "belly_pain": random.choice([True, False]),
        "abnormal_menstruation": random.choice([True, False]),
        "dischromic_patches": random.choice([True, False]),
        "watering_from_eyes": random.choice([True, False]),
        "increased_appetite": random.choice([True, False]),
        "polyuria": random.choice([True, False]),
        "family_history": random.choice([True, False]),
        "mucoid_sputum": random.choice([True, False]),
        "rusty_sputum": random.choice([True, False]),
        "lack_of_concentration": random.choice([True, False]),
        "visual_disturbances": random.choice([True, False]),
        "receiving_blood_transfusion": random.choice([True, False]),
        "receiving_unsterile_injections": random.choice([True, False]),
        "coma": random.choice([True, False]),
        "stomach_bleeding": random.choice([True, False]),
        "distention_of_abdomen": random.choice([True, False]),
        "history_of_alcohol_consumption": random.choice([True, False]),
        "fluid_overload1": random.choice([True, False]),
        "blood_in_sputum": random.choice([True, False]),
        "prominent_veins_on_calf": random.choice([True, False]),
        "palpitations": random.choice([True, False]),
        "painful_walking": random.choice([True, False]),
        "pus_filled_pimples": random.choice([True, False]),
        "blackheads": random.choice([True, False]),
        "scurring": random.choice([True, False]),
        "skin_peeling": random.choice([True, False]),
        "silver_like_dusting": random.choice([True, False]),
        "small_dents_in_nails": random.choice([True, False]),
        "inflammatory_nails": random.choice([True, False]),
        "blister": random.choice([True, False]),
        "red_sore_around_nose": random.choice([True, False]),
        "yellow_crust_ooze": random.choice([True, False]),
        "prognosis": random.choice([True, False])
    }
    return symptoms

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
    collection.insert_one(data.model_dump())
    
    results = predict_symptoms(data)
    # validated data
    return {"status": "Data received",
            "results": results}

def predict_symptoms(data: Symptoms):
    random_symptoms = generate_random_symptoms()
    symptoms_instance = Symptoms(**random_symptoms)
    symptoms_instance = symptoms_instance.model_dump()
    data = data.model_dump()
    for key in data:
        symptoms_instance[key] = data[key]
    model = pickle.load(open('model.pkl', 'rb'))
    symptoms_instance = pd.DataFrame([symptoms_instance])
    disease = model.predict(symptoms_instance)

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