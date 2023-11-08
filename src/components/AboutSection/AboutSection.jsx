// import libs:
import React from 'react';

// import static & assets:
import classess from './AboutSection.module.scss';

const AboutSection = ({name, description, cost, image}) => {
    return (
        <div className={classess.container}>
            <div className={classess.message}>
                <div className={classess.message__content}>
                    <div className={classess.message__card}>
                        <div className={classess.message__card__title}>
                            <div className={classess.message__card__img}>
                                <img src={image} alt="not alt"/>
                            </div>
                            <h1>
                                { name }
                            </h1>
                        </div>
                        <div className={classess.message__card__description}>
                            <p>
                                { description }
                            </p>
                            <div className={classess.cost}>
                                {cost
                                    ?
                                    <h2 style={{textAlign:"center"}}>
                                        Стоимость: { cost }₽ за занятие.
                                    </h2>
                                    :
                                    <h2>
                                        Занятия проводятся бесплатно.
                                    </h2>
                                }
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default AboutSection;