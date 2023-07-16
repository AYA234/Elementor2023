import axios from "axios"
let baseUrl="http://127.0.0.1:5000"
export const GetUserByEmailAndPassword=(email,password)=>{
    let dataToSend={
        "email":email,
        "password":password
    }
    return axios.post(`${baseUrl}/getUserByEmailAndPassword`,dataToSend)
  

}

export const getUserPackagesByUserId=(userId)=>{
    return axios.get(`${baseUrl}/getUserPackagesByUserId/${userId}`)
  

}

export const getLastSiteUsages = (siteId,time) =>{
    return axios.get(`${baseUrl}/getLastUsages/${siteId}/${time}`)
}

