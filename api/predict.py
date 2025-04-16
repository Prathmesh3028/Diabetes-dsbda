from http.server import BaseHTTPRequestHandler
import json
import os
import sys

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Get the request data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Extract features
            pregnancies = float(data.get('pregnancies', 0))
            glucose = float(data.get('glucose', 0))
            blood_pressure = float(data.get('bloodPressure', 0))
            skin_thickness = float(data.get('skinThickness', 0))
            insulin = float(data.get('insulin', 0))
            bmi = float(data.get('bmi', 0))
            diabetes_pedigree = float(data.get('diabetesPedigreeFunction', 0))
            age = float(data.get('age', 0))
            
            # Calculate risk score (simplified algorithm)
            # Higher values for glucose, BMI, age, and family history increase risk
            risk_score = (
                (glucose / 140) +  # Normalized glucose (140 mg/dL is high)
                (bmi / 35) +       # Normalized BMI (35+ is obese)
                (age / 50) +       # Normalized age (risk increases with age)
                (diabetes_pedigree * 2) +  # Family history is important
                (insulin < 50 and glucose > 120) * 0.5 +  # Low insulin + high glucose
                (pregnancies / 4)  # Multiple pregnancies slightly increase risk
            )
            
            # Determine prediction and probability
            is_diabetic = risk_score > 2.2
            probability = min(max(risk_score / 4.5, 0), 1)  # Scale to 0-1
            
            # Prepare the response
            response = {
                'prediction': int(is_diabetic),
                'probability': float(probability),
                'message': 'Diabetes detected' if is_diabetic else 'No diabetes detected',
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