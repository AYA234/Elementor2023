import * as React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import IconButton from '@mui/material/IconButton';
import ListItemButton from '@mui/material/ListItemButton';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import {Outlet, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { logOut } from '../redux/actions/userActions';
import ElementorLogo from './Screenshot 2023-07-13 153352.png';

const drawerWidth = 240;

function Layout(props) {
    const { window } = props;
    let isUserConnected = useSelector(x => x.usersReducer.isUserConnected)
    let curUser = useSelector(x => x.usersReducer.curUser)
    let dispach = useDispatch()
    let navigate = useNavigate()
 



    const container = window !== undefined ? () => window().document.body : undefined;

    return (
        <Box sx={{ display: 'flex' }}>
            <CssBaseline />
            <AppBar position="fixed"  >
                <Toolbar>
                <img src={ElementorLogo} alt="Elementor Logo" style={{ width: '60px', marginRight: '10px' }} />

                    <Typography variant="h6" noWrap component="div">       
                        Elementor     {isUserConnected ? curUser?.first_name: ''}
                    </Typography>
                    {!isUserConnected &&
                        <Typography >
                            <ListItemButton to='login'> Login/SignIn</ListItemButton>
                        </Typography>
                        ||
                        <Typography >
                            <ListItemButton onClick={() => {dispach(logOut());navigate('../')}}> Log out</ListItemButton>
                        </Typography>
                    }
                </Toolbar>
            </AppBar>        
            <Box
                component="main"
                sx={{ flexGrow: 1, p: 3, width: { sm: `calc(100% - ${drawerWidth}px)` } }}
            >
                <Toolbar />
                <Outlet />
            </Box>
        </Box>
    );
}

Layout.propTypes = {
    window: PropTypes.func,
};

export default Layout;