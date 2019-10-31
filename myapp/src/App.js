import React from 'react';
import {
  BrowserRouter,
  Switch,
  Route,
  Link
} from "react-router-dom";


import Name from "./Name";
import Home from './components/Home';
import Contact from './components/Contact';
import About from './components/About';
import Error from './components/Error';
import Navigation from './components/Navigation';

function App() {
  return (
    <BrowserRouter>
      <div>

        
        <Navigation />

        <nav>
          <ul>
            <li><Link to='/'>HomeTitle</Link></li>
            <li><Link to='/contact'>ContactTitle</Link></li>
            <li><Link to='/about'>AboutTitle</Link></li>
          </ul>
        </nav>


        <Switch>
          <Route path='/' component={Home} exact />
          <Route path='/contact' component={Contact} />
          <Route path='/about' component={About} />
          <Route component={Error} />
        </Switch>
      </div>
    </BrowserRouter>

  );
}


function HomeTitle()  {
  return (
    <h2>Home</h2>
  )
}
function AboutTitle()  {
  return (
    <h2>About</h2>
  )
}
function ContactTitle()  {
  return (
    <h2>Contact</h2>
  )
}

export default App;
