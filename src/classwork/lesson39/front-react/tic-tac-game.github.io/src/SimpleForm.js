import React, { useState } from 'react';

function SimpleForm() {
    const [formData, setFormData] = useState({playerX:'', playerO: ''});

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({...formData, [name]: value});
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Отправленные данные: ', formData)
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="playerX">Игрок X:</label>
                <input
                    type="text"
                    id="playerX"
                    name="playerX"
                    value={formData.playerX}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label htmlFor="playerO">Игрок O:</label>
                <input
                    type="text"
                    id="playerO"
                    name="playerO"
                    value={formData.playerO}
                    onChange={handleChange}
                    required
                />
            </div>
            <button type="submit">Отправить </button>
        </form>
    );
}

export default SimpleForm;