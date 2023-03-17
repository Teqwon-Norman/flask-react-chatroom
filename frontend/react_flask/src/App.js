import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Home from './pages/Home';
import './App.css';

function App() {
  // added code from me
  const [roomData, setRoomData] = useState(null)

  useEffect(() => {
    axios.get('/').then(res=> {
      setRoomData(({
        user_name: res.name,
        room_code: res.code,
        join: res.join,
        create: res.create
      })).catch((error) => {
        console.log(error.res)
        console.log(error.res.status)
        console.log(error.res.headers)
      })
    })
  })

  return (
    <div className="app">
      <Home />
    </div>
  );
}

export default App;
