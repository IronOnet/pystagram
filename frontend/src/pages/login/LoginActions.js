import axios from "axios"; 
//import {push } from "connected-react-router"
import {toast } from "react-toastify"; 
import { setAxiosAuthToken, toastOnError } from "../../utils/Utils";
import {useNavigate} from "react-router-dom";
import { SET_TOKEN, SET_CURRENT_USER, UNSET_CURREENT_USER, UNSET_CURRENT_USER } from "./LoginTypes";
import * as ROUTES from '../../constants/routes';

export const login = (userData, redirectTo) => dispatch =>{
    axios. 
        post("/api/v1/token/login/", userData) 
        .then(response =>{
            console.log(response)
            const {auth_token} = response.data; 
            setAxiosAuthToken(auth_token); 
            dispatch(setToken(auth_token)); 
            dispatch(getCurrentUser(redirectTo));
        })
        .catch(error =>{
            dispatch(unsetCurrentUser()); 
            console.log(error)
            toastOnError(error);
        });
};

export const getCurrentUser = redirectTo => dispatch =>{
    axios 
        .get("/api/v1/users/me/") 
        .then(response =>{
            const user = {
                username: response.data.username, 
                email: response.data.email
            }; 
            
            dispatch(setCurrentUser(user, redirectTo));
        })
        .catch(error =>{
            dispatch(unsetCurrentUser()); 
            if(error.response){
                if(error.response.status === 401 && 
                    error.response.hasOwnProperty("detail") &&
                    error.response.data["detail"] === "User inactive or deleted."){
                        // push resend activation here
                    }
            }
            else{
                toastOnError(error);
            }
        });
}; 

export const setCurrentUser = (user, redirectTo) => dispatch =>{
    const history = useNavigate();
    localStorage.setItem("user", JSON.stringify(user)); 
    dispatch({
        type: SET_CURRENT_USER, 
        payload: user
    });

    if(redirectTo !== ""){
        // TODO: Add push notification here
        //dispatch(push(redirectTo));
        history.push(redirectTo);
    }
}; 

export const setToken = token => dispatch =>{
    setAxiosAuthToken(""); 
    localStorage.removeItem("token");
    dispatch({
        type: SET_TOKEN, 
        payload: token
    });
}; 

export const unsetCurrentUser = () => dispatch =>{
    setAxiosAuthToken("") 
    localStorage.removeItem("token"); 
    localStorage.removeItem("user"); 
    dispatch({
        type: UNSET_CURRENT_USER
    });
}; 

export const logout = () => dispatch =>{
    const history = useNavigate();
    axios 
        .post("/api/v1/token/logout") 
        .then(response => {
            dispatch(unsetCurrentUser()); 
            history.push(ROUTES.DASHBOARD);
            toast.success("Logout successful");
        })
        .catch(error =>{
            dispatch(unsetCurrentUser()); 
            toastOnError(error);
        });
}