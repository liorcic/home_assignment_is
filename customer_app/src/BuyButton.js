import React from 'react';
import { Button } from 'react-bootstrap';
import axios from 'axios';

function BuyButton() {
  const handleClick = () => {
    axios.post(`${process.env.REACT_APP_API_URL}/buy`)
      .then(res => {
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  };

  return (
    <Button variant="primary" onClick={handleClick}>Random Buy</Button>
  );
}

export default BuyButton;
