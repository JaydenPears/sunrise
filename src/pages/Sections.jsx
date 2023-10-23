// import libs:
import { React, Fragment, useState, useEffect } from 'react';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';
import Select from 'react-select';
import MyCalendar from '../components/MyCalendar/MyCalendar';
import AboutSection from '../components/AboutSection/AboutSection';

// import static:
import classess from './../styles/Sections.module.scss';
import png from './../assets/basketball.png';

const Sections = () => {
    useScrollToTop();
    const [section, setSection] = useState(null);
    const [group, setGroup] = useState(null);

    const setNewSection = (newSection) => {
        setSection(newSection);
        setGroup(null);
    };

    const setNewGroup = (newGroup) => {
        setGroup(newGroup);
    };

    useEffect(() => {
        // console.log(section, group);
    }, [section, group]);

    const forSections = [
        {"value": "Баскетбол", "label": "Баскетбол"},
        {"value": "Большой Теннис", "label": "Большой Теннис"},
    ];

    const groups = {
        "Баскетбол": [
            {"value": "Баскетбол - Junior", "label": "Баскетбол - Junior"},
            {"value": "Баскетбол - Middle", "label": "Баскетбол - Middle"},
            {"value": "Баскетбол - Senior", "label": "Баскетбол - Senior"},
        ],
        "Большой Теннис": [
            {"value": "Большой Теннис - Junior", "label": "Большой Теннис - Junior"},
            {"value": "Большой Теннис - Middle", "label": "Большой Теннис - Middle"},
            {"value": "Большой Теннис - Senior", "label": "Большой Теннис - Senior"},
        ],
    };

    const infoAboutSections = {
        "Баскетбол": {
            "description": "Спортивная командная игра с мячом, в которой мяч забрасывают руками в кольцо соперника. В баскетбол играют две команды, каждая из которых состоит из пяти полевых игроков (замены не ограничены). Цель каждой команды — забросить мяч в кольцо с сеткой (корзину) соперника и помешать другой команде завладеть мячом и забросить его в свою корзину.",
            "cost": "200 рублей/занятие"
        },
        "Большой Теннис": {
            "description": "",
            "cost": ""
        }
    }

    return (
        <Fragment>
            <Helmet>
                <title>
                    Наши секции
                </title>
            </Helmet>
            <div className={classess.container}>
                <h1>
                    Наши секции
                </h1>
                <div className={classess.selector}>
                    <Select
                        className={classess.mySelect}
                        value={section}
                        options={forSections}
                        onChange={setNewSection}
                        placeholder={"Выберите секцию"}
                        isSearchable={false}
                        theme={(theme) => ({
                            ...theme,
                            colors: {
                                ...theme.colors,
                                primary25: '#d3d3d3',
                                primary50: '#d3d3d3',
                                primary: 'rgb(197, 135, 218)',
                            }
                        })}
                    />
                </div>
                {section !== null
                    ?
                    <div className={classess.layout}>
                        <AboutSection
                            name={section["value"]}
                            image={png}
                            description={infoAboutSections[section["value"]]["description"]}
                            cost={infoAboutSections[section["value"]]["cost"]}
                        />
                        <div className={classess.selector}>
                            <Select
                                className={classess.mySelect}
                                value={group}
                                options={section !== null
                                    ? groups[section["value"]]
                                    : []
                                }
                                onChange={setNewGroup}
                                placeholder={"Выберите группу"}
                                isSearchable={false}
                                theme={(theme) => ({
                                    ...theme,
                                    colors: {
                                        ...theme.colors,
                                        primary25: '#d3d3d3',
                                        primary50: '#d3d3d3',
                                        primary: 'rgb(197, 135, 218)',
                                    }
                                })}
                            />
                        </div>
                    </div>
                    :
                    <div/>
                }
                {group !== null
                    ? <MyCalendar />
                    : <div/>
                }
            </div>
        </Fragment>
    );
};

export default Sections;