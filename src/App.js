import { Fragment } from 'react';
import { Routes, Route } from 'react-router-dom';
import Footer from './components/Footer/Footer';
import Header from './components/Header/Header';
import ContactUs from './pages/ContactUs';
import Home from './pages/Home';
import AboutUs from './pages/AboutUs';
import News from './pages/News';
import Sections from './pages/Sections';
import Post from './pages/Post';

function App() {
    return (
        <Fragment>
            <Header />
            <Routes>
                <Route path="/news" element={<News />}/>
                <Route path="/contact_us" element={<ContactUs />}/>
                <Route path="/about_us" element={<AboutUs />}/>
                <Route path="/sections" element={<Sections />}/>
                <Route exact path="/" element={<Home />}/>
                <Route path="/news/:id" element={<Post />}/>
            </Routes>
            <Footer />
        </Fragment>
    );
}

export default App;