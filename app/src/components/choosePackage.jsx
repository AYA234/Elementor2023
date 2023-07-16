import { useEffect } from "react"
import { getUserPackagesByUserId } from '../axios/usersAxios'
import { useSelector } from "react-redux"
import { useState } from "react"
import { BasicCard } from "./card"
import { LinearProgress } from "@mui/material"

export const ChoosePackage = () => {
    const [packagesToUser, setPackagesToUser] = useState([])
    const[isWaitingToServerResponse,setIsWaitingToServerResponse]=useState(true)
    let curUser = useSelector(x => x.usersReducer.curUser)
    useEffect(() => {
        getUsersPackages(curUser)
    }, [])
    const getUsersPackages = (curUser) => {
        
        if (curUser)
            getUserPackagesByUserId(curUser.user_id).then(x => { setPackagesToUser(x.data['packages']);setIsWaitingToServerResponse(false) })
    }
    return <>
        {isWaitingToServerResponse && 
        <LinearProgress/>||
        <div>
        <h1>Your active packages:</h1>
        {packagesToUser.map((p, i) =>
            <div key={i} >
                <BasicCard package={p}></BasicCard>
                <br/>
            </div>
        )}
        </div>}

    </>
}