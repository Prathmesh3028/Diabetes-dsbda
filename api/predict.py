from http.server import BaseHTTPRequestHandler
import json
import os
import sys
import numpy as np

# Set environment variables for scikit-learn
os.environ['JOBLIB_TEMP_FOLDER'] = '/tmp'

# Simple prediction function without model loading
def predict_diabetes(features):
    """
    A simplified prediction function that doesn't rely on loading the model
    This allows deployment without needing to train/load the model on Vercel
    In a real app, you would use an API to a hosted model or optimize the model loading
    """
    # These are simplified rules based on medical knowledge
    # High glucose, BMI, and age are risk factors for diabetes
    glucose = features[0][1]  # Index 1 is glucose
    bmi = features[0][5]      # Index 5 is BMI
    age = features[0][7]      # Index 7 is age
    
    # Calculate a simple risk score (this is NOT a real medical model)
    risk_score = (glucose / 140) + (bmi / 35) + (age / 50)
    
    # Determine prediction and probability
    is_diabetic = risk_score > 2.1
    probability = min(max(risk_score / 4, 0), 1)  # Scale to 0-1
    
    return int(is_diabetic), float(probability)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Get the request data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Extract features
            features = np.array([
                [
                    float(data.get('pregnancies', 0)),
                    float(data.get('glucose', 0)),
                    float(data.get('bloodPressure', 0)),
                    float(data.get('skinThickness', 0)),
                    float(data.get('insulin', 0)),
                    float(data.get('bmi', 0)),
                    float(data.get('diabetesPedigreeFunction', 0)),
                    float(data.get('age', 0))
                ]
            ])
            
            # Make a prediction using the simplified function
            prediction, probability = predict_diabetes(features)
            
            # Prepare the response
            response = {
                'prediction': prediction,
                'probability': probability,
                'message': 'Diabetes detected' if prediction == 1 else 'No diabetes detected',
                'note': 'This is a simplified model for demonstration purposes only'
            }
            
            # Send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            # Handle errors
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
    
    def do_OPTIONS(self):
        # Handle CORS preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 