// import libs:
import { React, useState, useEffect } from 'react';
import { Text } from 'react-native';
import useScrollToTop from '../hooks/useScrollToTop';
import { useLocation } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import axios from 'axios';

// import static:
import classess from './../styles/Post.module.scss';

const Post = () => {
    useScrollToTop();
    const [title, setTitle] = useState('');
    const [news, setNews] = useState('');
    const [img, setImg] = useState('');
    const URL = `${process.env.REACT_APP_URL}`;

    const news_id = Number(useLocation().pathname.split('/').pop());

    useEffect(() => {
        axios.get(`${URL}/posts/${news_id}/`, {
            responseType: 'json',
            headers: {
                'Content-Type': 'application/json',
            }
        }).then((response) => {
            const data = response.data;
            setTitle(data.title);
            setNews(data.description);
            setImg(data.image);
        })
    }, [news_id, URL]);

    return (
        <div className={classess.container}>
            <Helmet>
                <title>{title}</title>
            </Helmet>
            <div className={classess.post}>
                <img
                    src={img}
                    className={classess.background_picture}
                    alt='must be an alt'
                />
                <h1>{ title }</h1>
                <div className={classess.post__description}>
                    <Text style={{fontSize: "1.7rem", textAlign: "left"}}>
                        { news }
                    </Text>
                </div>
            </div>
        </div>
    )
};

export default Post;