from http.server import BaseHTTPRequestHandler
import json

def handler(request, context):
    # This function is called by Vercel serverless
    headers = {
        'Content-type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
    
    response = {
        'status': 'active',
        'message': 'Diabetes Prediction API is running',
        'endpoints': {
            'predict': '/api/predict'
        },
        'version': '1.0.0'
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(response)
    }

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'status': 'active',
            'message': 'Diabetes Prediction API is running',
            'endpoints': {
                'predict': '/api/predict'
            },
            'version': '1.0.0'
        }
        
        self.wfile.write(json.dumps(response).encode())
        
    def do_OPTIONS(self):
        # Handle CORS preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 