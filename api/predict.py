from http.server import BaseHTTPRequestHandler
import json
import os
import sys
import numpy as np
import joblib

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

try:
    # Import the model training module
    from models.model_training import train_model
    
    # Paths to model files
    model_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'models', 'diabetes_model.pkl')
    scaler_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'models', 'scaler.pkl')
    
    # Create the models directory if it doesn't exist
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Train or load the model
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        print("Training a new model...")
        train_model()
    
    # Load the model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
except Exception as e:
    print(f"Error loading or training model: {e}")

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
            
            # Scale the features
            features_scaled = scaler.transform(features)
            
            # Make a prediction
            prediction = model.predict(features_scaled)[0]
            probability = model.predict_proba(features_scaled)[0][1]
            
            # Prepare the response
            response = {
                'prediction': int(prediction),
                'probability': float(probability),
                'message': 'Diabetes detected' if prediction == 1 else 'No diabetes detected'
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