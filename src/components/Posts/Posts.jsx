// import libs:
import React from 'react';

// import static & assets:
import classes from './Posts.module.scss';
import { BsArrowRight } from 'react-icons/bs';

import bg from './../../assets/background.avif';
import { Link } from 'react-router-dom';

const test_text = "Здесь будет располагаться некоторый текст, который пользователю будет показываться, как короткое описание";

const locationData = [
    { id: 1, location: test_text, isFeatured: true, img: bg },
    { id: 2, location: test_text, isFeatured: true, img: bg },
    { id: 3, location: test_text, isFeatured: false, img: bg },
    { id: 4, location: test_text, isFeatured: false, img: bg },
    { id: 5, location: test_text, isFeatured: false, img: bg },
    { id: 6, location: test_text, isFeatured: true, img: bg },
    { id: 7, location: test_text, isFeatured: true, img: bg },
    { id: 8, location: test_text, isFeatured: true, img: bg },
    { id: 9, location: test_text, isFeatured: false, img: bg },
];

const Posts = ({ page }) => {
    const mapData = !page ? locationData.slice(0, 3) : locationData;
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
                        {mapData.map(({ id, location, isFeatured, img }) => (
                            <Link to={`/news/${id}`} className={classes.gallery__item} key={id}>
                                <img
                                    src={img}
                                    alt={location}
                                    className={classes.gallery__item__img}
                                />
                                <div className={classes.overlay} />
                                <div className={classes.gallery__item__content}>
                                    
                                    <h2 className={classes.gallery__item__content__location}>
                                        {`${location.slice(0, 90)}...`}
                                    </h2>
                                </div>
                                {isFeatured
                                    ? <div className={classes.gallery__item__afisha}>Афиша | 23 января 2023 года</div>
                                    : <div className={classes.gallery__item__news}>Новость | 23 января 2023 года</div>
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