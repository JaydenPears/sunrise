// import libs:
import React, { Fragment } from 'react';
import Hero from '../components/Hero/Hero';
import Locations from '../components/Posts/Posts';
import Message from '../components/Message/Message';
import { Helmet } from 'react-helmet';
import useScrollToTop from '../hooks/useScrollToTop';

// import assets:
import photo from './../assets/trainer.jpg';

const Home = () => {
    useScrollToTop();

    return (
        <Fragment>
            <Helmet>
                <title>
                    Спортивный клуб "Восход"
                </title>
            </Helmet>
            <Hero />
            <Message
                isFirst={true}
                name="Даниил Давыдов"
                post="Директор АНО СК ВОСХОД"
                description=""
                image={photo}
            />
            <Locations />
        </Fragment>
    );
};

export default Home;