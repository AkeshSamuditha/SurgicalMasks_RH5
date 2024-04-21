import * as React from 'react';
import { navigationMenu } from './NavigationMenu'
import {useNavigate} from 'react-router-dom'
// import logo from '/Users/vihidun/MyFolder/Development/pulse/frontend/src/image2vector.svg'
import { Avatar, Button } from '@mui/material';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz'
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

function Navigation() {
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);
    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };
    const handleClose = () => {
        setAnchorEl(null);
    };
    const navigate = useNavigate();
    const handleLogout=()=>{
        console.log('logout')
        handleClose()
    }
  return (

    <div className='h-screen sticky top-0'>
        <div>
            <div className='py-5'>
            {/* <img src={logo} alt="" width={48} height={48} /> */}

                <p>User Panel</p>
            </div>
            <div className='space-y-80'>
            {navigationMenu.map((item) => (
                <div 
                key={item.title} // Ensure each item has a unique key
                className='cursor-pointer flex space-x-3 items-center'
                onClick={() => item.title === "Profile" ? navigate(`/profile/${5}`) : navigate(item.path)}
                >
                    {item.icon}
                    <span className='text-xl'>{item.title}</span>
                </div>
            ))}
            </div>
            
            
        </div>
    </div>
  )
}

export default Navigation