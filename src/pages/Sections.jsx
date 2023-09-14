import React, { Fragment } from 'react';
import Hero from '../components/Hero/Hero';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';

const Sections = () => {
    useScrollToTop();
    return (
        <Fragment>
            <Helmet>
                <title>
                    Наши секции
                </title>
            </Helmet>
            <Hero isDynamic>
                Наши секции
            </Hero>
        </Fragment>
    );
};

export default Sections;