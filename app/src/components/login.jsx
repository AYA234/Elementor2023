import { useRef } from 'react'
import { GetUserByEmailAndPassword } from '../axios/usersAxios'
import { fillCurrentUser } from '../redux/actions/userActions'

import { useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate } from "react-router-dom"

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Divider, Input } from '@mui/material';
import { Label } from '@mui/icons-material'

export const Login = () => {
    const [newUser, setNewUser] = useState(
        {
            isActive: true,
            idNumber: "",
            password: "",
            status: 0,
            email: "",
            phoneNumber: "",
            bornDate: new Date(Date.now()),
            fname: "",
            lname: "",
            address: "",
        }
    )
    const dispach = useDispatch()
    let naviagate = useNavigate()

    let password = useRef()
    let email = useRef()

     const logIn = () => {
        GetUserByEmailAndPassword(newUser.email, newUser.password).then(x => { dispach(fillCurrentUser(x.data)); naviagate('../choosePackage') })
    }
    return <>
        <Card style={{'width':'50rem','textAlign':'center','marginLeft':'20vw'}}>
            <CardContent>
                <Typography variant="h5" component="div">
                   Login
                </Typography>
                <br />
                <Divider />
                <h4>Email:</h4>
                <Input type="email" ref={email} onChange={(e) => {  setNewUser({ ...newUser, email: e.target.value }) }}></Input>
                <h4>Password::</h4>
                <Input type="password" ref={password} onChange={(e) => {  setNewUser({ ...newUser, password: e.target.value }) }}></Input>
            </CardContent>
            <br/>
            <Divider />
            <br/>
            <CardActions>
                <Button onClick={() => { logIn() }} size="small">LOGIN</Button>
            </CardActions>
        </Card>
    </>

}

// export default Login