import React from 'react'
import ReactDOM from 'react-dom'

// condictional render
const isLoading = true
const loadDate = () => {
    if (isLoading) {
        return <div>loading...</div>
    }
    return <div>loading finish.</div>
}

const element = (
    <h1>
        條件:
        {loadDate()}
    </h1>
)

ReactDOM.render(element, document.getElementById('root'))
