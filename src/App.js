// import libs:
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import { arrayRoutes } from "./router";

// import static:
import './static/styles/index.scss';
import classess from './static/styles/App.module.scss';

const App = () => {
    return (
        <div style={{display: "flex", flexDirection: "column"}}>
            <Header/>
            <div className={classess.container}>
                <Routes>
                    {arrayRoutes.map(route => 
                        <Route
                            key={route.id}
                            path={route.path}
                            element={route.element}
                            exact={route.exact}
                        />    
                    )}
                </Routes>
            </div>
        </div>
    )
};

export default App;