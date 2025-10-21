#!/usr/bin/env python3
"""
Single-server solution: Web server + Form submission handler
Saves rental applications as JSON files - No email functionality
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from datetime import datetime

SUBMISSIONS_DIR = "applications"
PORT = 8000

class ApplicationHTTPHandler(SimpleHTTPRequestHandler):
    """Handles both static files AND form submissions"""
    
    def do_POST(self):
        """Handle POST requests for form submission"""
        if self.path == '/submit_application':
            self.handle_form_submission()
        else:
            self.send_error(404, "Endpoint not found")
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def handle_form_submission(self):
        """Process form submission - Save to JSON file only"""
        try:
            # Get content length and read POST data
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            application_data = json.loads(post_data.decode('utf-8'))
            
            # Add metadata
            application_data['submittedAt'] = datetime.now().isoformat()
            application_data['submittedFrom'] = self.client_address[0]
            
            # Create submissions directory
            if not os.path.exists(SUBMISSIONS_DIR):
                os.makedirs(SUBMISSIONS_DIR)
            
            # Generate filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            first_name = application_data.get('firstName', 'Unknown').replace(' ', '_')
            last_name = application_data.get('lastName', 'Unknown').replace(' ', '_')
            filename = f"{timestamp}_{first_name}_{last_name}.json"
            filepath = os.path.join(SUBMISSIONS_DIR, filename)
            
            # Save to JSON file
            with open(filepath, 'w') as f:
                json.dump(application_data, f, indent=2)
            
            print(f"✅ Application saved: {filename}")
            
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
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.send_error(500, f"Server error: {str(e)}")
    
    def end_headers(self):
        """Add CORS headers to all responses"""
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run_server():
    """Start the combined web server"""
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, ApplicationHTTPHandler)
    
    print("=" * 70)
    print("🏢 PepperTree Townhomes - Application Submission Server")
    print("=" * 70)
    print(f"✅ Server running on port {PORT}")
    print(f"🌐 Website: http://localhost:{PORT}")
    print(f"📝 Application Form: http://localhost:{PORT}/rental-application-form.html")
    print(f"📁 Applications saved to: {os.path.abspath(SUBMISSIONS_DIR)}/")
    print("=" * 70)
    print("\n✨ Rental applications will be saved as JSON files")
    print("   No email functionality - files only\n")
    print("Press Ctrl+C to stop\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped")
        httpd.shutdown()

if __name__ == '__main__':
    run_server()
