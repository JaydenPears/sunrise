// import libs:
import { React, useState, useEffect } from 'react';
import axios from 'axios';

// import static & assets:
import classes from './Posts.module.scss';
import { BsArrowRight } from 'react-icons/bs';

import { Link } from 'react-router-dom';

const months = {
    1: "Января",
    2: "Февраля",
    3: "Марта",
    4: "Апреля",
    5: "Мая",
    6: "Июня",
    7: "Июля",
    8: "Августа",
    9: "Сентября",
    10: "Октября",
    11: "Ноября",
    12: "Декабря",
};

const getDate = (date) => {
    let year = date.split('-')[0];
    let month = Number(date.split('-')[1]);
    let day = Number(date.split('-')[2].split('T')[0]);
    return `${day} ${months[month]} ${year} года`;
}

const Posts = ({ page }) => {
    const URL = `${process.env.REACT_APP_URL}/posts/`;
    const [newsData, setNewsData] = useState([]);
    const [mapData, setMapData] = useState([]);

    useEffect(() => {
        axios.get(`${URL}`, {
            responseType: 'json',
            headers: {
                'Content-Type': 'application/json',
            }
        }).then((response) => {
            const data = response.data;
            setNewsData(data);
        })
    }, [page, URL]);

    useEffect(() => {
        if (newsData !== undefined) {
            setMapData(!page ? newsData.slice(0, 3) : newsData);
        }
    }, [newsData, page]);

    return (
        <div className={classes.container}>
            <div className={`${classes.locations} ${page ? classes.page : ""}`}>
                <div className={classes.locations__content}>
                    <h2 className={classes.locations__content__title}>
                        {!page
                            ? 'Последние новости'
                            : 'Все новости'
                        }
                    </h2>
                    <div className={classes.locations__content__gallery}>
                        {mapData.map(({ id, date, short_description, category, image }) => (
                            <Link to={`/news/${id}`} className={classes.gallery__item} key={id}>
                                <img
                                    src={image}
                                    alt={"must be an alt"}
                                    className={classes.gallery__item__img}
                                />
                                <div className={classes.overlay} />
                                <div className={classes.gallery__item__content}>
                                    
                                    <h2 className={classes.gallery__item__content__location}>
                                        {`${short_description}`}
                                    </h2>
                                </div>
                                {category === "afisha"
                                    ?
                                    <div className={classes.gallery__item__afisha}>
                                        Афиша | {getDate(date)}
                                    </div>
                                    :
                                    <div className={classes.gallery__item__news}>
                                        Новость | {getDate(date)}
                                    </div>
                                }
                            </Link>
                        ))}
                    </div>
                    {!page && (
                        <div className={classes.locations__content__viewmore}>
                            <Link to="/news">
                                Перейти ко всем новостям <BsArrowRight />
                            </Link>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Posts;