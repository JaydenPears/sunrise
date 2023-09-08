// import libs:
import React, { useEffect, useState } from 'react';
import { Link } from "react-router-dom";
import { BiMenuAltRight } from 'react-icons/bi';
import { AiOutlineClose } from 'react-icons/ai';

// import static:
import classess from './Header.module.scss';

const Header = () => {
    const [menuOpen, setMenuOpen] = useState(false);
    const [size, setSize] = useState({
        width: undefined,
        height: undefined,
    });

    useEffect(() => {
        const handleResize = () => {
            setSize({
                width: window.innerWidth,
                height: window.innerHeight,
            })
        }
        window.addEventListener("resize", handleResize);

        return () => window.removeEventListener("resize", handleResize);
    }, [])

    useEffect(() => {
        if (size.width > 768 && menuOpen) {
            setMenuOpen(false);
        }
    }, [size.width, menuOpen])

    const menuToggleHandler = () => {
        setMenuOpen((p) => !p);
    }

    return (
        <header className={classess.header}>
            <div className={classess.header__content}>
                    <Link to="" className={classess.header__content__logo}>
                        <p>Восход</p>
                    </Link>
                <nav
                    className={`${classess.header__content__nav} ${menuOpen ? classess.isMenu : ''}`}
                >
                    <ul>
                        <li>
                            <Link to='/page_one'>О нас</Link>
                        </li>
                        <li>
                            <div className="linkLayout">
                                <Link to='/page_two'>Тренерский состав</Link>
                            </div>
                        </li>
                        <li>
                            <Link to='/page_three'>Секции</Link>
                        </li>
                    </ul>
                    <button>Связаться с нами</button>
                </nav>
                <div className={classess.header__content__toggle}>
                    {!menuOpen ? <BiMenuAltRight onClick={menuToggleHandler}/> : <AiOutlineClose onClick={menuToggleHandler}/>}
                </div>
            </div>
        </header>
    )
};

export default Header;