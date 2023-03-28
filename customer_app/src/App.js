import './App.css';
import BuyList from './PurchaseHistory';
import React, { useState, useEffect } from 'react';
import BuyButton from './BuyButton';
import axios from 'axios';

function App() {

  const [buyList, setList] = useState([]);
  const [userIdFilter, setUserIdFilter] = useState('');


  const reloadTable = () => {
    axios.get(`${process.env.REACT_APP_API_URL}/buyList`)
      .then(res => {
        setList(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }

  const reloadByFilter = () => {
    axios.get(`${process.env.REACT_APP_API_URL}/buyList/${userIdFilter}`)
      .then(res => {
        setList(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }

  useEffect(() => {
    reloadTable();
  }, []);

  return (
    <div className="App">
      <h1>Home Assignment FrontEnd</h1>
      <div className="filter-container">
        <input type="text" placeholder="User Id" value={userIdFilter} onChange={event => setUserIdFilter(event.target.value)} />
        <button onClick={reloadByFilter}>Search</button>
      </div>
      <BuyList buyList={buyList}/>
      <BuyButton />
      <button onClick={reloadTable}>Reload Table</button>
    </div>
  );
}

export default App;
