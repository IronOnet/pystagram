import {useState, useEffect, useContext } from "react"; 
import AxiosContext from "../context/axios";

export default function useAuthListener(){
    const [user, setUser] = useState(JSON.parse(localStorage.getItem('authUser'))); 
    const {axios } = useContext(AxiosContext); 

    useEffect(()=>{
        // TODO: WIP
    });
}