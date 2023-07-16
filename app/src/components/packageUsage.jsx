import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { getTotalPackageUsage } from '../axios/packagesAxios'
import { useState } from "react"
import ProgressBar from "./progressBar"
import { Button } from "@mui/material"
import { useNavigate } from "react-router"
import {setCurrentSiteIdToReview} from '../redux/actions/sitesActions'


const PackageUsage = () => {

  let currentPackage = useSelector(x => x.packagesReducer).currentPackage
  let navigate=useNavigate()
  let dispach=useDispatch()
  let resources = [
    'total_cpu_percent',
    'total_cpu_tic',
    'total_disc_a_gb',
    'total_disc_b_gb',
    'total_storage_gb'
  ]

  useEffect(() => {
    getTotalPackageUsage(currentPackage.package_id).then(x => { setPackageUsage(x.data) })

  }, [])

  const [packageCapacity, setPackageCapacity] = useState({
    'total_cpu_percent': 0,
    'total_cpu_tic': 0,
    'total_disc_a_gb': 0,
    'total_disc_b_gb': 0,
    'total_disc_cache': 0,
    'total_storage_gb': 0
  })
  const [packagUsage, setPackageUsage] = useState({
    'total_cpu_percent': 0,
    'total_cpu_tic': 0,
    'total_disc_a_gb': 0,
    'total_disc_b_gb': 0,
    'total_disc_cache': 0,
    'total_storage_gb': 0
  })
  return <>
    <h2>The total usage for package number {currentPackage.package_id} :</h2>

    {resources.map((x, i) => (
      <div key={i}>
        <h3>{x} : {parseInt( packagUsage[x]/1000)} %</h3>
        <ProgressBar value={packagUsage[x]/1000} ></ProgressBar>
        <br />
      </div>
    ))}

<h2>To see more details about usage per site ,choose your site:</h2>
    {currentPackage.sites_per_package.map((site, i) => (
      <div key={i}>
       <Button key={i} onClick={()=>{dispach(setCurrentSiteIdToReview(site.site_id));navigate('../sitePreview')}}>{site.site_name}</Button>
      </div>
    ))}
  
  </>
}

export default PackageUsage