import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Crear el objeto JSON
        response = {
            "message": "Hello from the Python API!"
        }
        
        # Enviar la respuesta en formato JSON
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return