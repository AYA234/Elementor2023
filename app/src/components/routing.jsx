import { BrowserRouter, Route, Routes } from "react-router-dom"
import Layout from "./layout"
import { ChoosePackage } from "./choosePackage"
import {SitePreview} from '../components/sitePreview'
import PackageUsage from "./packageUsage"
import { Login } from "./login"

export const Routing = () => {
    return <>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route path="/" element={<Login/>}></Route>
                    <Route path="choosePackage" element={<ChoosePackage/>}></Route>
                    <Route path="packageUsage" element={<PackageUsage/>}></Route>
                    <Route path='login' element={<Login/>}></Route>
                    <Route path="sitePreview" element={<SitePreview/>}></Route>

                </Route>
            </Routes>
        </BrowserRouter>
    </>
}