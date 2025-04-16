from http.server import BaseHTTPRequestHandler
import json

def handler(request, context):
    # This function is called by Vercel serverless
    headers = {
        'Content-type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps({'status': 'healthy'})
    }

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'healthy'}).encode())
    
    def do_OPTIONS(self):
        # Handle CORS preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 