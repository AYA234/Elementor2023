import axios from "axios"
let baseUrl="http://127.0.0.1:5000"
export const getTotalPackageUsage=(packagId)=>{
    return axios.get(`${baseUrl}/getTotalPackageUsage/${packagId}`)
}