// import libs:
import { React, useEffect, useState } from 'react';
import Select from 'react-select';

// import static:
import classess from './MySelect.module.scss';
 
const MySelect = ({options, parentCallback, placeholder}) => {
    const [selectOptions, setSelectOptions] = useState(null);

    const handleChange = (selectedOption) => {
        parentCallback(selectedOption["value"]);
    };

    useEffect(() => {
        setSelectOptions(null);
        setSelectOptions(options);
    }, [options]);
 
    return (
        <div>
            <div className={classess.select}>
                <Select
                    options={selectOptions}
                    onChange={handleChange}
                    placeholder={placeholder}
                    isSearchable={false}
                    theme={(theme) => ({
                        ...theme,
                        colors: {
                          ...theme.colors,
                          primary25: '#d3d3d3',
                          primary50: '#d3d3d3',
                          primary: 'rgb(197, 135, 218)',
                        },
                    })}
                />
            </div>
        </div>
    );
}
 
export default MySelect;