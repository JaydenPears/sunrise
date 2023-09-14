import React, { Fragment } from 'react';
import Hero from '../components/Hero/Hero';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';

const LearnMore = () => {
    useScrollToTop();
    return (
        <Fragment>
            <Helmet>
                <title>
                    Информация о нас
                </title>
            </Helmet>
            <Hero isDynamic>Подробнее о нас</Hero>
        </Fragment>
    );
};

export default LearnMore;