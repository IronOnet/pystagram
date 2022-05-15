import { useState, useContext, useEffect } from 'react'; 
import { Link, useHistory } from 'react-router-dom'; 
import * as ROUTES from '../constants/routes'; 
import AxiosContext from '../context/axios'; 


export default function Login(){

    const history = useHistory(); 
    const { axios } = useContext(AxiosContext); 

    const [emailAddress, setEmailAddress] = useState(''); 
    const [password, setPassword] = useState('');
    const [error, setError] = useState(''); 
    const isInvalid = password === '' || emailAddress === ''; 

    const handleLogin = async (event) =>{
        event.preventDefault();

        // Call the axios service to handle the login
    }

    useEffect(() =>{
        document.title = "Login - Pystagram";
    }, []);

    
    return <p>Login Page</p>
};