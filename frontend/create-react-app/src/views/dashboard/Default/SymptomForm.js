import { Button, Checkbox } from '@mui/material';
import MainCard from 'ui-component/cards/MainCard';

const SymptomForm = () => {
  return (
    <MainCard>
      <h1>What are your symptoms?</h1>
      <form>
          <div>
            <Checkbox id="formy-urine" />
            <label htmlFor="formy-urine">Formy Urine</label>
          </div>
          <div>
            <Checkbox id="nausea" />
            <label htmlFor="nausea">Nausea</label>
          </div>
          <div>
            <Checkbox id="itching" />
            <label htmlFor="itching">Itching</label>
          </div>
          <div>
            <Checkbox id="loss-of-appetite" />
            <label htmlFor="loss-of-appetite">Loss of Appetite</label>
          </div>
          <div>
            <Checkbox id="continuous-feel-of-urine" />
            <label htmlFor="continuous-feel-of-urine">Continuous Feel of Urine</label>
          </div>
          <div>
            <Checkbox id="lack-of-concentration" />
            <label htmlFor="lack-of-concentration">Lack of Concentration</label>
          </div>
          <div>
            <Checkbox id="breathlessness" />
            <label htmlFor="breathlessness">Breathlessness</label>
          </div>
          <div>
            <Checkbox id="vomiting" />
            <label htmlFor="vomiting">Vomiting</label>
          </div>
          <div>
            <Checkbox id="fatigue" />
            <label htmlFor="fatigue">Fatigue</label>
          </div>
          <div>
            <Checkbox id="fever" />
            <label htmlFor="fever">Fever</label>
          </div>
          <div>
            <Checkbox id="headache" />
            <label htmlFor="headache">Headache</label>
          </div>
        <div>
          <Checkbox id="swelling" />
          <label htmlFor="swelling">Swelling</label>
        </div>
        <div>
          <Checkbox id="pain" />
          <label htmlFor="pain">Pain</label>
        </div>
        <div>
          <Checkbox id="weight-loss" />
          <label htmlFor="weight-loss">Weight Loss</label>
        </div>
        <div>
          <Checkbox id="weakness" />
          <label htmlFor="weakness">Weakness</label>
        </div>
        <div>
          <Checkbox id="dizziness" />
          <label htmlFor="dizziness">Dizziness</label>
        </div>
        <div>
          <Checkbox id="confusion" />
          <label htmlFor="confusion">Confusion</label>
        </div>
        <div>
          <Checkbox id="dry-mouth" />
          <label htmlFor="dry-mouth">Dry Mouth</label>
        </div>
        <div>
          <Checkbox id="constipation" />
          <label htmlFor="constipation">Constipation</label>
        </div>
        <div>
          <Checkbox id="diarrhea" />
          <label htmlFor="diarrhea">Diarrhea</label>
        </div>
        <div>
          <Checkbox id="sweating" />
          <label htmlFor="sweating">Sweating</label>
        </div>
        <Button variant="contained" color="primary">
          Check Symptoms
        </Button>
      </form>
    </MainCard>
  );
};
export default SymptomForm;
