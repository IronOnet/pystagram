import {lazy, Suspense } from "react"; 
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import * as ROUTES_C from './constants/routes';
import Login from './pages/login/login.js'; 
import TestPageView from "./pages/test.js";
import Signup from "./pages/signup/signup.js";




const Index = () =>{
  return <h1>Hello Crazy World!!!</h1>
}

const TestView = () =>{
  return (<h1>Testing View!!</h1>)
}

//const Login = lazy(() =>require('./pages/login'));

//const ViewTest = lazy(()=> require('./pages/test'));


function App() {
  return (
   <Router>
     <Suspense fallback={<p>Loading...</p>}>
       <Routes>
         <Route path="/" element={<Index/>}/>
         <Route path="/login" element={<Login/>}/>
         <Route path="/sign-up" element={<Signup/>}/>
        
         <Route path="/test2" element={<TestPageView/>}/>
        
       </Routes>
     </Suspense>
   </Router>
  );
}

export default App;
