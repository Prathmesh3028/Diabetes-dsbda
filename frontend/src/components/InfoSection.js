import React from 'react';
import { Card } from 'react-bootstrap';

function InfoSection() {
  return (
    <Card className="mb-4">
      <Card.Body>
        <Card.Title>About Diabetes Prediction</Card.Title>
        <Card.Text>
          This application uses machine learning to predict the risk of diabetes based on several health metrics.
          Enter your health parameters in the form and get an instant prediction of your diabetes risk.
        </Card.Text>
        <Card.Text>
          <strong>Note:</strong> This tool is for educational purposes only and should not replace professional medical advice.
          Always consult with a healthcare provider for proper diagnosis and treatment.
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default InfoSection; 