// import libs:
import { React, Fragment, useState, useEffect } from 'react';
import useScrollToTop from '../hooks/useScrollToTop';
import { Helmet } from 'react-helmet';

// import static:
import classess from './../styles/Sections.module.scss';
import MySelect from '../components/MySelect/MySelect';

const Sections = () => {
    useScrollToTop();
    const [section, setSection] = useState(null);
    const [group, setGroup] = useState(null);

    const setNewSection = (newSection) => {
        setSection(newSection);
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
                <MySelect
                    parentCallback={setNewSection}
                    options={forSections}
                    placeholder={"Выберите секцию"}
                />
                {section !== null
                    ? 
                    <MySelect
                        parentCallback={setNewGroup}
                        options={groups[section]}
                        placeholder={"Выберите группу"}
                    />
                    :
                    <div/>
                }
            </div>
        </Fragment>
    );
};

export default Sections;