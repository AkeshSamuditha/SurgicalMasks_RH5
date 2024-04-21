import { Grid } from '@mui/material'
import React from 'react'
import Header from '../Header/Header'
import Banner from '../Banner/Banner'
import Paper from '@mui/material/Paper';
import { styled } from '@mui/material/styles';
import Navigation from '../Navigation/Navigation';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

// const Item = () => ({})


function HomePage() {

  
  return (
    <>
      <Header />
      <Banner />
      {/* <Navigation /> */}
      
    <Grid container xs={12} className='px-5 lg:px-36 justify-between'>
        <Grid item xs={3}  className='hidden lg:block w-full relative'>
            <Item elevation={1} >
              <Navigation />
            </Item>
        </Grid>

        <Grid item xs={6}  className='hidden lg:block w-full relative'>

              <Item elevation={0}>middle part</Item>

      
        </Grid>

        <Grid item xs={3}  className='hidden lg:block w-full relative'>

            <Item elevation={0}>right part</Item>

            
        </Grid>
    </Grid>
    </>
    
    

  )
}

export default HomePage