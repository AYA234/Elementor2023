import Produce from "immer"

const packagesState = {
    currentPackage: {
        'package_id': 0,
        'sites_per_package': [
            {
                site_description: '',
                site_id: 0,
                site_name: ''
            }
        ],
        'cost_per_month': 0,
        'cpu_percent': 0,
        'cpu_tic': 0,
        'disc_a_gb': 0,
        'disc_b_gb': 0,
        'disc_cache': 0,
        'torage_gb': 0


    }

}

export const packagesReducer = Produce(
    (s, a) => {
        switch (a.type) {
            case 'SET-CURRENT-PACKAGE':
                s.currentPackage = a.payload
                break;
            default:
                break;
        }
    }, packagesState
)
export default packagesReducer




