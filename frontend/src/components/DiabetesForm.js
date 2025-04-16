import React, { useState } from 'react';
import { Form, Button, Card, Row, Col, Alert } from 'react-bootstrap';

const initialFormState = {
  pregnancies: '',
  glucose: '',
  bloodPressure: '',
  skinThickness: '',
  insulin: '',
  bmi: '',
  diabetesPedigreeFunction: '',
  age: ''
};

function DiabetesForm({ onSubmit, isLoading, isDisabled }) {
  const [formData, setFormData] = useState(initialFormState);
  const [validated, setValidated] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const form = e.currentTarget;
    
    setValidated(true);
    
    if (form.checkValidity() === false) {
      e.stopPropagation();
      return;
    }
    
    onSubmit(formData);
  };

  return (
    <Card className="form-container">
      <Card.Body>
        <Card.Title>Enter Health Parameters</Card.Title>
        
        {isDisabled && (
          <Alert variant="warning" className="mb-3">
            The backend server is not available. Please ensure the Python backend is running.
          </Alert>
        )}
        
        <Form noValidate validated={validated} onSubmit={handleSubmit}>
          <Row>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="pregnancies">
                <Form.Label>Number of Pregnancies</Form.Label>
                <Form.Control
                  type="number"
                  name="pregnancies"
                  value={formData.pregnancies}
                  onChange={handleChange}
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid number.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="glucose">
                <Form.Label>Glucose (mg/dL)</Form.Label>
                <Form.Control
                  type="number"
                  name="glucose"
                  value={formData.glucose}
                  onChange={handleChange}
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid glucose level.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
          </Row>

          <Row>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="bloodPressure">
                <Form.Label>Blood Pressure (mm Hg)</Form.Label>
                <Form.Control
                  type="number"
                  name="bloodPressure"
                  value={formData.bloodPressure}
                  onChange={handleChange}
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid blood pressure.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="skinThickness">
                <Form.Label>Skin Thickness (mm)</Form.Label>
                <Form.Control
                  type="number"
                  name="skinThickness"
                  value={formData.skinThickness}
                  onChange={handleChange}
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid skin thickness.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
          </Row>

          <Row>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="insulin">
                <Form.Label>Insulin (mu U/ml)</Form.Label>
                <Form.Control
                  type="number"
                  name="insulin"
                  value={formData.insulin}
                  onChange={handleChange}
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid insulin level.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="bmi">
                <Form.Label>BMI (kg/m²)</Form.Label>
                <Form.Control
                  type="number"
                  name="bmi"
                  value={formData.bmi}
                  onChange={handleChange}
                  step="0.1"
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid BMI.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
          </Row>

          <Row>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="diabetesPedigreeFunction">
                <Form.Label>Diabetes Pedigree Function</Form.Label>
                <Form.Control
                  type="number"
                  name="diabetesPedigreeFunction"
                  value={formData.diabetesPedigreeFunction}
                  onChange={handleChange}
                  step="0.001"
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid value.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group className="mb-3" controlId="age">
                <Form.Label>Age (years)</Form.Label>
                <Form.Control
                  type="number"
                  name="age"
                  value={formData.age}
                  onChange={handleChange}
                  required
                  min="0"
                  disabled={isDisabled || isLoading}
                />
                <Form.Control.Feedback type="invalid">
                  Please enter a valid age.
                </Form.Control.Feedback>
              </Form.Group>
            </Col>
          </Row>

          <div className="d-grid gap-2">
            <Button 
              variant="primary" 
              type="submit" 
              disabled={isDisabled || isLoading}
            >
              {isLoading ? 'Processing...' : 'Predict Diabetes Risk'}
            </Button>
          </div>
        </Form>
      </Card.Body>
    </Card>
  );
}

// Set default props
DiabetesForm.defaultProps = {
  isDisabled: false
};

export default DiabetesForm; 