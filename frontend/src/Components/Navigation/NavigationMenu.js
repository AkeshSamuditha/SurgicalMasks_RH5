import HomeIcon from "@mui/icons-material/Home"
import MapIcon from '@mui/icons-material/Map';
import CoronavirusIcon from '@mui/icons-material/Coronavirus';
import ExploreIcon from "@mui/icons-material/Explore"
import NotificationIcon from "@mui/icons-material/Notifications"
import MessageIcon from "@mui/icons-material/Message"
import ListAltIcon from "@mui/icons-material/ListAlt"
import GroupIcon from "@mui/icons-material/Group"
import AccountCircleIcon from "@mui/icons-material/AccountCircle"
import PendingIcon from "@mui/icons-material/Pending"

export const navigationMenu = [
    {
        title:"Dashboard",
        icon:<HomeIcon/>,
        path:"/home"
    },
    {
        title:"Explore",
        icon:<MapIcon/>,
        path:"/explore"
    },
    {
        title:"Outbreaks",
        icon:<CoronavirusIcon/>,
        path:"/Outbreaks"
    },
    {
        title:"Notification",
        icon:<NotificationIcon/>,
        path:"/Notification"
    },
    // {
    //     title:"Lists",
    //     icon:<ListAltIcon/>,
    //     path:"/lists"
    // },
    // {
    //     title:"Communities",
    //     icon:<GroupIcon/>,
    //     path:"/communities"
    // },
    // {
    //     title:"Profile",
    //     icon:<AccountCircleIcon/>,
    //     path:"/profile"
    // },
    {
        title:"More",
        icon:<PendingIcon/>,
        path:"/more"
    },
]