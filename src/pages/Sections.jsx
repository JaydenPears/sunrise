// import libs:
import React, { Fragment } from 'react';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';

// import static:
import classess from './../styles/Sections.module.scss';
import MySelect from '../components/MySelect/MySelect';

const Sections = () => {
    useScrollToTop();
    return (
        <Fragment>
            <Helmet>
                <title>
                    Наши секции
                </title>
            </Helmet>
            <div className={classess.container}>
                <h1>
                    Наши секции
                </h1>
                <MySelect/>
            </div>
        </Fragment>
    );
};

export default Sections;