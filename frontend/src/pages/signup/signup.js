import {useState, useContext, useEffect} from 'react'; 
import {Link, useHistory, useNavigate} from 'react-router-dom'; 
import *  as ROUTES from '../../constants/routes'; 

//TODO: Add a method to check whether the username already exists 

export default function SignUp(){
    const history = useNavigate(); 

    // axios context will go here 

    const [userName, setUserName] = useState('');
    const [fullName, setFullName] = useState('');
    const [emailAddress, setEmailAddress] = useState(''); 
    const [password, setPassword] = useState(''); 
    const [password2, setConfirmPassword] = useState('');

    const [error, setError] = useState(''); 
    const isInvalid = password === '' || password !== password2 || emailAddress === ''; 

    const handleSignup = async (event) =>{
        event.preventDefault();
        console.log("Signup button clicked!!")
        // logic to handle signup goes here
    }

    useEffect(() =>{
        document.title = 'Sign Up - Pystagram';
    }, []); 

    return (
        <div className="container flex mx-auto max-w-screen-md items-center h-screen">
            <div className="flex w-3/5">
                <img src="/images/iphone-with-profile.jpg" alt="Iphone with instagram app"/>
            </div>
            <div className="flex flex-col w-2/5">
                <div className="flex flex-col items-center bg-white p-4 border border-gray-primary mb-4 rounded">
                    <h1 className="flex justify-center w-full">
                        <img src="/images/logo.png" alt="Pystagram" className="mt-2 w-6/12 mb-4"/>

                    </h1>
                    {error && <p className="mb-4 text-xs text-red-primary">{error}</p>}

                    <form onSubmit={handleSignup} method="POST">
                        <input 
                            aria-label="Enter your username"
                            type="text" 
                            placeholder="Username"
                            className="text-sm text-gray w-full mr-3 py-5 px-4 h-2 border border-gray-primary rounded mb-2"
                            onChange={({target}) => setUserName(target.value)} 
                            value={userName}/>

                        <input 
                            aria-label="Enter your full name"
                            type="text" 
                            placeholder="Full name"
                            className="text-sm text-gray w-full mr-3 py-5 px-4 h-2 border border-gray-primary rounded mb-2"
                            onChange={({target}) => setFullName(target.value)} 
                            value={fullName}/>

                        <input 
                            aria-label="Enter your email address"
                            type="text" 
                            placeholder="Email address"
                            className="text-sm text-gray w-full mr-3 py-5 px-4 h-2 border border-gray-primary rounded mb-2"
                            onChange={({target}) => setEmailAddress(target.value)} 
                            value={emailAddress}/>

                        <input 
                            aria-label="Enter your password"
                            type="password" 
                            placeholder="Password"
                            className="text-sm text-gray w-full mr-3 py-5 px-4 h-2 border border-gray-primary rounded mb-2"
                            onChange={({target}) => setPassword(target.value)} 
                            value={password}/>

                        <input 
                            aria-label="Confirm password"
                            type="password" 
                            placeholder="Confirm Password"
                            className="text-sm text-gray w-full mr-3 py-5 px-4 h-2 border border-gray-primary rounded mb-2"
                            onChange={({target}) => setUserName(target.value)} 
                            value={password}/>


                        


                        <button 
                            disabled={isInvalid} 
                            type="submit" 
                            className={`bg-blue-medium text-white w-full rounded h-8 font-bold ${isInvalid && 'opacity-50'}`}>
                                Sign Up
                        </button>



                    </form>
                </div>
                <div className="flex justify-center items-center flex-col w-full bg-white p-4 rounded border border-gray-primary">
                    <p className="text-sm">
                        Have an account?{` `}
                        <Link to={ROUTES.LOGIN} className="font-bold text-blue-medium">
                            Login
                        </Link>
                    </p>
                </div>
            </div>
        </div>
    );
};
