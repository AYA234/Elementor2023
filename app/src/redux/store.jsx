import { combineReducers, createStore } from "redux";
import usersReducer from "./reducers/usersReducer";
import packagesReducer from "./reducers/packagsRduces";
import {sitesReducer} from '../redux/reducers/sitesReducer'

export const reducer=combineReducers({usersReducer,packagesReducer,sitesReducer})
export const str=createStore(reducer)
window.store=str
export default str