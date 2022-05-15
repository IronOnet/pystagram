import {lazy, Suspense } from "react"; 
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import * as ROUTES_C from './constants/routes';

const Login = lazy(() => import('./pages/login'));

function App() {
  return (
   <Router>
      <Suspense fallbazck={<p>Loading...</p>}>
        <Routes>
          <Route path={ROUTES_C.LOGIN} component={Login} />
        </Routes>
      </Suspense>
   </Router>
  );
}

export default App;
