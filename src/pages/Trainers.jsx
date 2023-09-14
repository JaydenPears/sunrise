import React, { Fragment } from 'react';
import Hero from '../components/Hero/Hero';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';

const Pricing = () => {
    useScrollToTop();
    return (
        <Fragment>
            <Helmet>
                <title>
                    Тренерский состав
                </title>
            </Helmet>
            <Hero isDynamic>Тренерский состав</Hero>
        </Fragment>
    );
};

export default Pricing;