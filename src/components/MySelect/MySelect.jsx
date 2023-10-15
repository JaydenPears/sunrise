// import libs:
import React, { useState } from 'react';
import Select from 'react-select';

// import static:
import classess from './MySelect.module.scss';
 
const MySelect = () => {
    const [selectedOption, setSelectedOption] = useState(null);
 
    const handleChange = (selectedOption) => {
        setSelectedOption(selectedOption);
        console.log(`Option selected:`, selectedOption);
    };
 
    const options = [
        { value: 'helene', label: 'Helene' },
        { value: 'berline', label: 'Berline' },
        { value: 'selene', label: 'Selene' }
    ];
 
    return (
        <div>
            <div className={classess.select}>
                <Select
                    options={options}
                    onChange={handleChange}
                    placeholder="Favourite artists"
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