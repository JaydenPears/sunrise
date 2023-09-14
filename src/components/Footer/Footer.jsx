// import libs:
import React from 'react';
import { Link } from 'react-router-dom';

// import static:
import classes from './Footer.module.scss';
import { FaTelegram, FaVk } from 'react-icons/fa';

const socials = [
    {id: 1, icon: <FaTelegram />, link: "https://t.me/sunrise_russia"},
    {id: 2, icon: <FaVk />, link: "https://vk.com/sunrise.russia"},
];

const Footer = () => {
    return (
        <div className={classes.container}>
            <footer className={classes.footer}>
                <div className={classes.footer__base}>
                    <ul className={classes.footer__base__socials}>
                        {socials.map(({id, icon, link}) => (
                            <li key={id + 1}>
                                <Link target="_blank" rel="noopener noreferrer" to={link}>{icon}</Link>
                            </li>
                        ))}
                    </ul>
                    <span className={classes.footer__base__year}>
                        Спортивный клуб "Восход"&nbsp;&copy;&nbsp;{new Date().getFullYear()}
                    </span>
                </div>
            </footer>
        </div>
    );
};

export default Footer;