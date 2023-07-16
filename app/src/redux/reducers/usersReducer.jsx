import Produce from "immer"

const usersState = {
    curUser: {
        id: -1,
        isActive: true,
        idNumber: "",
        password: "",
        status: 2,
        email: "",
        phoneNumber: "",
        bornDate: Date.now(),
        fname: "",
        lname: "",
        address: ""

    },
    isUserConnected:false
}

export const usersReducer = Produce(
    (s, a) => {
        switch (a.type) {
            
            case 'SET-CURRENT-USER':         
                s.curUser = a.payload
                s.isUserConnected=true
                break;
            case 'LOG-OUT':       
                s.curUser={
                    id: -1,
                    isActive: true,
                    idNumber: "",
                    password: "",
                    status: -1,
                    email: "",
                    phoneNumber: "",
                    bornDate: Date.now(),
                    fname: "",
                    lname: "",
                    address: ""
            
                }
                s.isUserConnected=false         
           
            default:
                break;
        }
    }, usersState
)
export default usersReducer




