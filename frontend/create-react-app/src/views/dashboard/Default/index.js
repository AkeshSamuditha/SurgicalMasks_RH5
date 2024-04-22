import { useEffect, useState } from 'react';

// material-ui
import { Grid } from '@mui/material';

import TotalGrowthBarChart from './TotalGrowthBarChart';
import { gridSpacing } from 'store/constant';
import SymptomForm from './SymptomForm';
import TableauEmbed from './TableauEmbed';

// ==============================|| DEFAULT DASHBOARD ||============================== //

const Dashboard = () => {
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(false);
  }, []);

  return (
    <Grid container spacing={gridSpacing}>
      <Grid item xs={12}>
        <Grid container spacing={gridSpacing}>
          <Grid item lg={4} md={6} sm={6} xs={12}>
            {/* <EarningCard isLoading={isLoading} /> */}
          </Grid>
          <Grid item lg={4} md={6} sm={6} xs={12}>
            {/* <TotalOrderLineChartCard isLoading={isLoading} /> */}
          </Grid>
          <Grid item lg={4} md={12} sm={12} xs={12}>
            <Grid container spacing={gridSpacing}>
              <Grid item sm={6} xs={12} md={6} lg={12}>
                {/* <TotalIncomeDarkCard isLoading={isLoading} /> */}
              </Grid>
              <Grid item sm={6} xs={12} md={6} lg={12}>
                {/* <TotalIncomeLightCard isLoading={isLoading} /> */}
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
      <Grid item xs={12}>
        <Grid container spacing={gridSpacing}>
          <Grid item xs={12} md={8}>
            <TotalGrowthBarChart isLoading={isLoading} />
            <TableauEmbed />
          </Grid>
          <Grid item xs={12} md={4}>
            <SymptomForm />
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Dashboard;
