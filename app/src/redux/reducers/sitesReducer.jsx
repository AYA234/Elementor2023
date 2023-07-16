import Produce from "immer"
  
const sitesState = {
  lastUsage:[],
  currenSiteId:'2'
}
  
export const sitesReducer = Produce(
    (s, a) => {
        switch (a.type) {
            case 'FILL-LAST-USAGE':
                s. lastUsage = a.payload
                break;
            case 'SET-CURRENT-SITE-ID':
                s.currenSiteId=a.payload
                break;
            case 'SET-CURRENT-SITE-ID-TO-REVIEW':
                s.currentSiteId = a.payload
                break;
            default:
                break;
        }
    }, sitesState
)
export default sitesReducer




