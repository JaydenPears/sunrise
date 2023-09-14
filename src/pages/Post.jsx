// import libs:
import React from 'react';
import useScrollToTop from '../hooks/useScrollToTop';
import { useLocation } from 'react-router-dom';
import { Helmet } from 'react-helmet';

// import static:
import classess from './../styles/Post.module.scss';

const Post = () => {
    useScrollToTop();
    const news_id = Number(useLocation().pathname.split('/').pop());
    const news_title = 'Новость о событии'

    return (
        <div className={classess.container}>
            <Helmet>
                <title>{news_title}</title>
            </Helmet>
            <div className={classess.post}>
                <h1>Новость № {news_id}</h1>
            </div>
        </div>
    )
};

export default Post;