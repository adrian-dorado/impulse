import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './Homepage.js';
import Footer from './Footer.js';
import './App.css';
import NavBar from "./NavBar";
import SignUpForm from './SignUpForm';
import AboutUs from './AboutUs';

import './index.css';

export default function App() {
  return (
    <BrowserRouter>
        <NavBar />
      <div className="container">
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='footer' element={<Footer />} />

        </Routes>


        <Routes>
          {/* <Route path='/' element={<Homepage />} /> */}
          <Route path='signup/' element={<SignUpForm />} />
          <Route path='aboutus/' element={<AboutUs />} />

        </Routes>
      </div>
    </BrowserRouter>

  );
};