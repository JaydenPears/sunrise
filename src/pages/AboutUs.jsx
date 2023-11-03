// import libs:
import React, { Fragment, useState, useEffect } from 'react';
import Hero from '../components/Hero/Hero';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';
import Message from './../components/Message/Message';
import axios from 'axios';

// import static:
import './../styles/AboutUs.module.scss';

const LearnMore = () => {
    useScrollToTop();
    const [personal, setPersonal] = useState([]);
    const URL = `${process.env.REACT_APP_URL}/personal/`;

    useEffect(() => {
        axios.get(`${URL}`, {
            responseType: 'json',
            headers: {
                'Content-Type': 'application/json',
            }
        }).then((response) => {
            const data = response.data;
            setPersonal(data);
        })
    }, [URL]);

    return (
        <Fragment>
            <Helmet>
                <title>
                    Информация о нас
                </title>
            </Helmet>
            <Hero isDynamic>Подробнее о нас</Hero>
            {personal.map((_, index) => (
                <Message
                    isRight={index % 2 === 0
                        ? true
                        : false
                    }
                    key={index}
                    name={personal[index].fio}
                    post={personal[index].job[0]}
                    description={personal[index].description}
                    image={personal[index].image}
                />
            ))}
        </Fragment>
    );
};

export default LearnMore;