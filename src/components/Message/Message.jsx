// import libs:
import React from 'react';

// import static & assets:
import classess from './Message.module.scss';
import photo from './../../assets/trainer.jpg';

const Message = () => {
    return (
        <div className={classess.container}>
            <div className={classess.message}>
                <div className={classess.message__content}>
                    {/* <h1 className={classess.message__title}>
                        Президент Спортивного клуба
                    </h1> */}
                    <div className={classess.message__card}>
                        <div className={classess.message__card__title}>
                            <div className={classess.message__card__img}>
                                <img src={photo} alt="not alt"/>
                            </div>
                            <div className={classess.message__card__text}>
                                <h1>
                                    Даниил Давыдов
                                </h1>
                                <h2 className={classess.message__card__text__decoration}>
                                    Директор АНО СК ВОСХОД
                                </h2>
                            </div>
                        </div>
                        <div className={classess.message__card__description}>
                            <p>
                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eius earum modi, autem officiis maiores dolorem beatae recusandae odio cumque id. Accusantium in laudantium nulla commodi tempora maxime recusandae iure blanditiis. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Expedita, voluptates ad delectus tempore eveniet incidunt rerum atque consectetur quod voluptatum omnis consequatur. Maxime inventore laborum obcaecati ad totam, hic nihil. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores veritatis laudantium velit commodi vel numquam, sed fugiat ut. Cumque magni perspiciatis placeat et quaerat fuga vel magnam reiciendis animi sunt!
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default Message;