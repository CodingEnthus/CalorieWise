// src/components/CalorieForm.js
import React, { useState } from 'react';
import axios from 'axios';
import { Form, Button, Card, Alert } from 'react-bootstrap';

function CalorieForm() {
  const [food, setFood] = useState('');
  const [amount, setAmount] = useState('');
  const [calories, setCalories] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/calories', {
        food,
        amount,
      });
      setCalories(res.data.calories);
      setError('');
    } catch (err) {
      setCalories(null);
      setError(err.response?.data?.error || 'Something went wrong');
    }
  };

  return (
    <Card className="p-4 mt-4 shadow">
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Food</Form.Label>
          <Form.Control
            type="text"
            placeholder="e.g. rice"
            value={food}
            onChange={e => setFood(e.target.value)}
          />
        </Form.Group>
        <Form.Group className="mt-3">
          <Form.Label>Amount (grams)</Form.Label>
          <Form.Control
            type="number"
            placeholder="e.g. 100"
            value={amount}
            onChange={e => setAmount(e.target.value)}
          />
        </Form.Group>
        <Button variant="primary" type="submit" className="mt-3 w-100">
          Get Calories
        </Button>
      </Form>

      {calories && (
        <Alert variant="success" className="mt-4">
          Total Calories: <strong>{calories}</strong>
        </Alert>
      )}
      {error && (
        <Alert variant="danger" className="mt-4">
          {error}
        </Alert>
      )}
    </Card>
  );
}

export default CalorieForm;
