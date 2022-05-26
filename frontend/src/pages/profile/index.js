import {useParams, useNavigate} from "react"; 
import {useState, useEffect} from "react"; 
import {getUserByUsername}  from "../../services/axios"; 
import * as ROUTES from "../../constants/routes";
import Header from "../../components/header";
import UserProfile from "../../components/profile";



export default function Profile(){
    const {username } = useParams(); 
    const [user, setUser] = useState(null); 
    const navigate = useNavigate(); 

    useEffect(()=>{
        async function checkUserExists(){
            const [user] = await getUserByUsername(username); 
            if (user?.userId){
                setUser(user);
            } else{
                navigate(ROUTES.NOT_FOUND)
            }
        }
        checkUserExists();
    }, [username, navigate]);


    return user?.username ?(
        <div className="bg-gray-background">
            <Header/>
            <div className="mx-auto max-w-screen-lg">
                <UserProfile user={user}/>
            </div>
        </div>
    ): null;
}