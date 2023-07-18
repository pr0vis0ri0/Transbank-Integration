import React, { useState } from 'react'

export default function Counter() {
    const [currentValue, setCurrentValue] = useState(5);

    return (
        <div>
            <h1>Contador</h1>
            <p>Valor actual : {currentValue}</p>
            <div>
                <button onClick={() => setCurrentValue((oldState) => oldState + 1)}>+</button>
                <button onClick={() => setCurrentValue((oldState) => oldState - 1)}>-</button>
            </div>
        </div>
    )
}