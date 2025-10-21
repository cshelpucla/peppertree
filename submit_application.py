#!/usr/bin/env python3
"""
Rental Application Submission Handler
Receives form data and stores it in JSON files
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from datetime import datetime
from urllib.parse import parse_qs
import cgi

# Configuration
SUBMISSIONS_DIR = "applications"
PORT = 8001

class ApplicationHandler(BaseHTTPRequestHandler):
    """Handle rental application submissions"""
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        """Handle POST request with application data"""
        if self.path == '/submit':
            try:
                # Get content length
                content_length = int(self.headers.get('Content-Length', 0))
                
                # Read and parse JSON data
                post_data = self.rfile.read(content_length)
                application_data = json.loads(post_data.decode('utf-8'))
                
                # Add metadata
                application_data['submittedAt'] = datetime.now().isoformat()
                application_data['submittedFrom'] = self.client_address[0]
                
                # Create submissions directory if it doesn't exist
                if not os.path.exists(SUBMISSIONS_DIR):
                    os.makedirs(SUBMISSIONS_DIR)
                
                # Generate unique filename with timestamp
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                applicant_name = f"{application_data.get('firstName', 'Unknown')}_{application_data.get('lastName', 'Unknown')}"
                applicant_name = applicant_name.replace(' ', '_').replace('/', '_')
                filename = f"{timestamp}_{applicant_name}.json"
                filepath = os.path.join(SUBMISSIONS_DIR, filename)
                
                # Save application data to JSON file
                with open(filepath, 'w') as f:
                    json.dump(application_data, f, indent=2)
                
                # Log submission
                print(f"✅ Application received: {applicant_name} - Saved to {filename}")
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {
                    'success': True,
                    'message': 'Application submitted successfully',
                    'filename': filename,
                    'timestamp': application_data['submittedAt']
                }
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except json.JSONDecodeError as e:
                # JSON parsing error
                self.send_error(400, f"Invalid JSON: {str(e)}")
                print(f"❌ JSON Error: {e}")
                
            except Exception as e:
                # General error
                self.send_error(500, f"Server error: {str(e)}")
                print(f"❌ Error processing application: {e}")
        else:
            self.send_error(404, "Endpoint not found")
    
    def log_message(self, format, *args):
        """Custom log format"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {format % args}")

def run_server():
    """Start the application submission server"""
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, ApplicationHandler)
    
    print("=" * 70)
    print("🏢 PepperTree Townhomes - Application Submission Server")
    print("=" * 70)
    print(f"✅ Server running on port {PORT}")
    print(f"📁 Storing applications in: {os.path.abspath(SUBMISSIONS_DIR)}/")
    print(f"🔗 Endpoint: http://localhost:{PORT}/submit")
    print(f"📋 Ready to receive applications...")
    print("=" * 70)
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        httpd.shutdown()

if __name__ == '__main__':
    run_server()
