#!/bin/bash
# Start both web server and application submission server

echo "🚀 Starting PepperTree Townhomes Servers..."
echo ""

# Kill any existing servers
pkill -9 -f "http.server" 2>/dev/null
pkill -9 -f "submit_application.py" 2>/dev/null
sleep 1

# Start the web server (port 8000)
echo "🌐 Starting web server on port 8000..."
cd /home/cshelp/peppertree
python3 -m http.server 8000 > /dev/null 2>&1 &
WEB_PID=$!

sleep 2

# Start the application submission server (port 8001)
echo "📋 Starting application submission server on port 8001..."
python3 /home/cshelp/peppertree/submit_application.py &
APP_PID=$!

sleep 2

echo ""
echo "✅ Servers started successfully!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 Website:          http://localhost:8000"
echo "📋 Application Form: http://localhost:8000/rental-application-form.html"
echo "🔧 Submission API:   http://localhost:8001/submit"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📁 Applications will be saved to: ./applications/"
echo ""
echo "🛑 To stop servers: pkill -f 'http.server|submit_application'"
echo ""
