// import libs:
import {React} from 'react';
import {Text, StyleSheet} from 'react-native';
import useScrollToTop from '../hooks/useScrollToTop';
import { useLocation } from 'react-router-dom';
import { Helmet } from 'react-helmet';

// import static:
import classess from './../styles/Post.module.scss';
import background from './../assets/background.avif';

const Post = () => {
    useScrollToTop();
    const news_id = Number(useLocation().pathname.split('/').pop());
    const news_title = 'Заголовок'.toUpperCase();
    const news = `С 4-6 октября в городе Иваново проходит Кубок организаций Госкорпорации «Росатом» по баскетболу 3х3 «Оранжевый атом», где принимает участие один из наших тренеров Ольга Зосименко в составе женской сборной Российского Химико-Технологического Университета им. Д.И.Менделеева \n\nСегодня уже второй день соревнований - стадия плей-офф. В 13:40 состоится игра за выход в полуфинал против команды из Казанского Государственного Энергнетического Университета! Подключайтесь к трансляции, смотрите и болейте!`;

    return (
        <div className={classess.container}>
            <Helmet>
                <title>{news_title}</title>
            </Helmet>
            <div className={classess.post}>
                <img
                    src={background}
                    className={classess.background_picture}
                    alt='must be an alt'
                />
                <h1>{ news_title }</h1>
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