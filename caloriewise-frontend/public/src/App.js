import React from 'react';
import CalorieForm from './components/CalorieForm';
import { Container } from 'react-bootstrap';
function App() {
  return (
    <Container className="mt-5">
      <h1 className="text-center">CalorieWise</h1>
      <CalorieForm />
    </Container>
  );
}
export default App;