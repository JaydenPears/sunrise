// import libs:
import { React, Fragment, useState, useEffect } from 'react';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';
import Select from 'react-select';

// import static:
import classess from './../styles/Sections.module.scss';

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
        console.log(section, group);
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
                    <div className={classess.selector}>
                        <Select
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
                    :
                    <div/>
                }
            </div>
        </Fragment>
    );
};

export default Sections;