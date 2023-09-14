// import libs:
import React, { Fragment } from 'react';
import Button from '../../UI/Button/Button';

// import static & assets:
import classes from './Hero.module.scss';
import background from './../../assets/background.avif'

const HomePageContent = () => {
    return (
        <Fragment>
            <h1 className={classes.hero__content__title_sunrise}>"Восход"</h1>
            <span className={classes.hero__content__tagline}>
                Спортивный клуб твоей мечты
            </span>
            <p className={classes.hero__content__description}>
                У нас присутствует много различных секций, <br />а в коллективах процветает командный дух.<br/>Всё на твой вкус!
            </p>
            <div className={classes.hero__content__cta}>
                <Button to="/contact_us">Присоединяйся!</Button>
                <Button to="/about_us" outline>
                    Прочесть больше
                </Button>
            </div>
        </Fragment>
    );
};

const Hero = ({ isDynamic, children }) => {
    return (
        <div className={classes.container}>
            <img
                src={background}
                className={classes.background_picture}
                alt='must be an alt'
            />
            <div className={classes.hero}>
                <div className={classes.hero__content}>
                    {!isDynamic && <HomePageContent />}
                    {isDynamic && <h1 className={classes.hero__content__title}>{children}</h1>}
                </div>
            </div>
        </div>
    );
};

export default Hero;