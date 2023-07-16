export const fillCurrentUser=(value)=>{
    return {type:'SET-CURRENT-USER',payload:value}
}

export const logOut=()=>{
    return {type:'LOG-OUT'}
}
