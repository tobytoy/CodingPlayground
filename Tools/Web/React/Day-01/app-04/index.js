import React from 'react'
import ReactDOM from 'react-dom'

const element = (
    <h1 className="title">
        Hello JSX.
        <span />
    </h1>
)

ReactDOM.render(element, document.getElementById('root'))