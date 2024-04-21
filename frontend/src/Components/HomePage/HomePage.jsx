import { Grid } from '@mui/material'
import React from 'react'
import Header from '../Header/Header'
import Banner from '../Banner/Banner'

function HomePage() {
  return (
    <>
      <Header />
      <Banner />
      
    <Grid container xs={12} className='px-5 lg:px-36 justify-between'>
        <Grid item xs={0} lg={2.5} className='hidden lg:block w-full relative'>
            <p className='text-center'>left part</p>
        </Grid>
        <Grid item xs={12} lg={6} className='hidden lg:block w-full relative'>

              <p className='text-center'>middle part</p>

      
        </Grid>
        <Grid item xs={0} lg={3} className='hidden lg:block w-full relative'>

            <p className='text-center'>right part</p>

            
        </Grid>
    </Grid>
    </>
    
    

  )
}

export default HomePage