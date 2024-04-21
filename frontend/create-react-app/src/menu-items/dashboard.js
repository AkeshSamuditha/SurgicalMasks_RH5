// assets
// import { IconDashboard } from '@tabler/icons-react';
import DashboardIcon from '@mui/icons-material/Dashboard';
import MapIcon from '@mui/icons-material/Map';
import CoronavirusIcon from '@mui/icons-material/Coronavirus';
import NotificationIcon from "@mui/icons-material/Notifications"
import GroupIcon from "@mui/icons-material/Group"

// constant
const icons = { DashboardIcon, MapIcon, CoronavirusIcon, NotificationIcon, GroupIcon };

// ==============================|| DASHBOARD MENU ITEMS ||============================== //

const dashboard = {
  id: 'User Panel',
  title: 'User Panel',
  type: 'group',
  children: [
    {
      id: 'default',
      title: 'Dashboard',
      type: 'item',
      url: '/dashboard/default',
      icon: icons.DashboardIcon,
      breadcrumbs: false
    },
    {
      id: 'default',
      title: 'Explore',
      type: 'item',
      url: '/dashboard/default',
      icon: icons.MapIcon,
      breadcrumbs: false
    },
    {
      id: 'default',
      title: 'Outbreaks',
      type: 'item',
      url: '/dashboard/default',
      icon: icons.CoronavirusIcon,
      breadcrumbs: false
    },
    {
      id: 'default',
      title: 'Notification',
      type: 'item',
      url: '/dashboard/default',
      icon: icons.NotificationIcon,
      breadcrumbs: false
    },
    {
      id: 'default',
      title: 'Communities',
      type: 'item',
      url: '/dashboard/default',
      icon: icons.GroupIcon,
      breadcrumbs: false
    },
  ]
};

export default dashboard;
