
// // src/components/ResultCard.js
// import React from 'react';
// import { Alert } from 'react-bootstrap';

// // Simple calorie chart (per 100g)
// const calorieChart = {
//   rice: 130,
//   bread: 265,
//   apple: 52,
//   banana: 89,
//   egg: 155,
//   milk: 42,
// };

// function ResultCard({ food, amount }) {
//   if (!food || !amount) return null;

//   const foodKey = food.toLowerCase();
//   const caloriesPer100g = calorieChart[foodKey];

//   if (!caloriesPer100g) {
//     return (
//       <Alert variant="danger" className="mt-4">
//         Sorry, we don't have data for <strong>{food}</strong>
//       </Alert>
//     );
//   }

//   const totalCalories = (caloriesPer100g * amount) / 100;

//   return (
//     <Alert variant="success" className="mt-4">
//       Total Calories in <strong>{amount}g {food}</strong>: <strong>{totalCalories} Calories</strong>
//     </Alert>
//   );
// }

// export default ResultCard;
// src/components/ResultCard.js
import React from "react";
import { Card } from "react-bootstrap";

function ResultCard({ food, amount, calories }) {
  if (!calories) return null; // Don't show card until we have a result

  return (
    <Card className="mt-4 shadow-lg">
      <Card.Body>
        <Card.Title className="text-center">Calorie Result</Card.Title>
        <Card.Text className="text-center">
          <strong>{food}</strong> ({amount} g) contains{" "}
          <strong>{calories} kcal</strong>.
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default ResultCard;
