import React, { useState } from 'react';
import { Button, Checkbox, FormControlLabel } from '@mui/material';
import MainCard from 'ui-component/cards/MainCard'; // Adjust the import path based on your project structure

const SymptomForm = () => {
  const [symptoms, setSymptoms] = useState({
    itching: false,
    skin_rash: false,
    nodal_skin_eruptions: false,
    continuous_sneezing: false,
    shivering: false,
    chills: false,
    joint_pain: false,
    stomach_pain: false,
    acidity: false,
    ulcers_on_tongue: false,
    muscle_wasting: false,
    vomiting: false,
    burning_micturition: false,
    spotting_urination: false,
    fatigue: false,
    weight_gain: false,
    anxiety: false,
    cold_hands_and_feets: false,
    mood_swings: false,
    weight_loss: false,
    restlessness: false,
    lethargy: false,
    patches_in_throat: false,
    irregular_sugar_level: false,
    cough: false,
    high_fever: false,
    sunken_eyes: false,
    breathlessness: false,
    sweating: false,
    dehydration: false,
    indigestion: false,
    headache: false,
    yellowish_skin: false,
    dark_urine: false,
    nausea: false,
    loss_of_appetite: false,
    pain_behind_the_eyes: false,
    back_pain: false,
    constipation: false,
    abdominal_pain: false,
    diarrhoea: false,
    mild_fever: false,
    yellow_urine: false,
    yellowing_of_eyes: false,
    acute_liver_failure: false,
    fluid_overload: false,
    swelling_of_stomach: false,
    swelled_lymph_nodes: false,
    malaise: false,
    blurred_and_distorted_vision: false,
    phlegm: false,
    throat_irritation: false,
    redness_of_eyes: false,
    sinus_pressure: false,
    runny_nose: false,
    congestion: false,
    chest_pain: false,
    weakness_in_limbs: false,
    fast_heart_rate: false,
    pain_during_bowel_movements: false,
    pain_in_anal_region: false,
    bloody_stool: false,
    irritation_in_anus: false,
    neck_pain: false,
    dizziness: false,
    cramps: false,
    bruising: false,
    obesity: false,
    swollen_legs: false,
    swollen_blood_vessels: false,
    puffy_face_and_eyes: false,
    enlarged_thyroid: false,
    brittle_nails: false,
    swollen_extremeties: false,
    excessive_hunger: false,
    extra_marital_contacts: false,
    drying_and_tingling_lips: false,
    slurred_speech: false,
    knee_pain: false,
    hip_joint_pain: false,
    muscle_weakness: false,
    stiff_neck: false,
    swelling_joints: false,
    movement_stiffness: false,
    spinning_movements: false,
    loss_of_balance: false,
    unsteadiness: false,
    weakness_of_one_body_side: false,
    loss_of_smell: false,
    bladder_discomfort: false,
    foul_smell_of_urine: false,
    continuous_feel_of_urine: false,
    passage_of_gases: false,
    internal_itching: false,
    toxic_look_typhos: false,
    depression: false,
    irritability: false,
    muscle_pain: false,
    altered_sensorium: false,
    red_spots_over_body: false,
    belly_pain: false,
    abnormal_menstruation: false,
    dischromic_patches: false,
    watering_from_eyes: false,
    increased_appetite: false,
    polyuria: false,
    family_history: false,
    mucoid_sputum: false,
    rusty_sputum: false,
    lack_of_concentration: false,
    visual_disturbances: false,
    receiving_blood_transfusion: false,
    receiving_unsterile_injections: false,
    coma: false,
    stomach_bleeding: false,
    distention_of_abdomen: false,
    history_of_alcohol_consumption: false,
    blood_in_sputum: false,
    prominent_veins_on_calf: false,
    palpitations: false,
    painful_walking: false,
    pus_filled_pimples: false,
    blackheads: false,
    scurring: false,
    skin_peeling: false,
    silver_like_dusting: false,
    small_dents_in_nails: false,
    inflammatory_nails: false,
    blister: false,
    red_sore_around_nose: false,
    yellow_crust_ooze: false,
    prognosis: false
  });

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      console.log('Symptoms:', symptoms);
      const response = await fetch('https://rude-wren-surgicalmasks.koyeb.app/symptoms', {
  method: 'POST',
  mode: 'no-cors', // Set mode to 'no-cors' to disable CORS
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ symptoms })
});
      if (response.ok) {
        const data = await response.json();
        console.log('Success:', data);
      }
    } catch (error) {
      console.error('Error:', error.error);
    }
  };

  const handleChange = (event) => {
    setSymptoms({ ...symptoms, [event.target.name]: event.target.checked });
  };

  return (
    <MainCard title="What are your symptoms?">
      <form onSubmit={handleSubmit}>
        <div style={{ maxHeight: '600px', overflowY: 'auto' }}>
          {' '}
          {Object.keys(symptoms).map((key, index) => (
            <FormControlLabel
              key={`${key}-${index}`} // Concatenate the key with index
              control={<Checkbox checked={symptoms[key]} onChange={handleChange} name={key} />}
              label={key.replace(/_/g, ' ').replace(/\b\w/g, (l) => l.toUpperCase())}
            />
          ))}
        </div>
        <br />
        <Button type="submit" variant="contained" color="primary">
          Check Symptoms
        </Button>
      </form>
    </MainCard>
  );
};

export default SymptomForm;
