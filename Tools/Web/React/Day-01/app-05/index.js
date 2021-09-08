import React from 'react'
import ReactDOM from 'react-dom'

let name = 'Toby'
let age = 20

const element = (
    <h1>
        Hello JSX, my name is {name} and my age is {age}!!
    </h1>
)

ReactDOM.render(element, document.getElementById('root'))
