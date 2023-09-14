// import libs:
import React, { Fragment } from 'react';
import Hero from '../components/Hero/Hero';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';

const ContactUs = () => {
    useScrollToTop();
    return (
        <Fragment>
            <Helmet>
                <title>
                    Связаться с нами
                </title>
            </Helmet>
            <Hero isDynamic>Связаться с нами</Hero>
        </Fragment>
    );
};

export default ContactUs;