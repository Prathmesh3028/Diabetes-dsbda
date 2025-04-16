import React from 'react';
import { Card, Alert, Spinner, ProgressBar } from 'react-bootstrap';

function PredictionResult({ result, loading, error }) {
  if (loading) {
    return (
      <Card className="result-container">
        <Card.Body className="text-center">
          <Card.Title>Analyzing Your Data</Card.Title>
          <div className="my-4">
            <Spinner animation="border" role="status" variant="primary">
              <span className="visually-hidden">Loading...</span>
            </Spinner>
          </div>
          <Card.Text>
            Please wait while our model analyzes your health data...
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }

  if (error) {
    return (
      <Card className="result-container">
        <Card.Body>
          <Card.Title>Error</Card.Title>
          <Alert variant="danger" className="mt-3">
            {error}
          </Alert>
          <Card.Text>
            Please try again or contact support if the problem persists.
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }

  if (!result) {
    return (
      <Card className="result-container">
        <Card.Body>
          <Card.Title>Prediction Results</Card.Title>
          <Card.Text className="text-muted mt-3">
            Fill out the form and submit to see your diabetes risk prediction.
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }

  const riskPercentage = Math.round(result.probability * 100);
  const riskVariant = result.prediction === 1 ? "danger" : "success";
  const riskClass = result.prediction === 1 ? "high-risk" : "low-risk";

  return (
    <Card className="result-container">
      <Card.Body>
        <Card.Title>Prediction Results</Card.Title>
        
        <div className="mt-4">
          <h5 className={`${riskClass} mb-3`}>
            {result.message}
          </h5>
          
          <Card.Text>
            Based on the information provided, our model predicts:
          </Card.Text>
          
          <Card.Text className="mb-2">
            <strong>Risk Level:</strong> {riskPercentage}%
          </Card.Text>
          
          <ProgressBar 
            variant={riskVariant} 
            now={riskPercentage} 
            className="mb-4" 
          />
          
          <Card.Text className="mt-3 small text-muted">
            This prediction is based on machine learning analysis of your health parameters. 
            Remember that this is not a medical diagnosis. 
            Please consult with a healthcare professional for proper evaluation.
          </Card.Text>
        </div>
      </Card.Body>
    </Card>
  );
}

export default PredictionResult; 