import * as React from 'react';

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Divider } from '@mui/material';
import {setCurrentPackage}from '../redux/actions/packagesActions'
import {  useNavigate } from "react-router-dom"
import { useDispatch } from 'react-redux';


export const BasicCard = (props) => {
    let naviagate = useNavigate()
    let dispach=useDispatch()

    return (
        <Card>
            <CardContent>
                <Typography variant="h5" component="div">
                    Package number: {props.package.package_id}
                </Typography>
                <br/>
                <Divider/>
                {props.package.sites_per_package.length==0 && <h4>No active sites in this package.</h4> ||
                <h4>Sites included in the package:</h4>}
                {props.package.sites_per_package.map((s) => (
                    <>
                        <Typography sx={{ mb: 1.5 }} color="text.secondary" key={s.site_id}>
                            {s.site_name}
                        </Typography>
                    </>
                ))}
            </CardContent>
            <CardActions>
                <Button onClick={()=>{dispach(setCurrentPackage(props.package));naviagate('../packageUsage')}} size="small">See package details</Button>
            </CardActions>
        </Card>
    );
};
