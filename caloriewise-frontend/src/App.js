import React from 'react';
import ResultCard from './components/ResultCard';
import CalorieForm from './components/CalorieForm';
import { Container } from 'react-bootstrap';
function App() {
  return (
    <Container className="mt-5">
      <h1 className="text-center">CalorieWise</h1>
      <CalorieForm />
      <ResultCard />
    </Container>
  );
}
export default App;