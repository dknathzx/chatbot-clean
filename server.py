# server.py
# Pure Python web server — no Flask, no libraries!

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse
from chatbot import get_response  # importing your brain!

PORT = 8000

class ChatHandler(BaseHTTPRequestHandler):

    # --- Serve the HTML page when browser opens the URL ---
    def do_GET(self):
        if self.path == "/":
            # Open and send your index.html file
            with open("index.html", "r") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

    # --- Handle messages sent from the browser ---
    def do_POST(self):
        if self.path == "/chat":
            # Read the message from browser
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length)
            data = json.loads(body)

            user_message = data.get("message", "")

            # Get response from your chatbot brain
            bot_reply = get_response(user_message)

            # Send reply back to browser as JSON
            response = json.dumps({"reply": bot_reply})
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))

    # Suppress server log noise in terminal
    def log_message(self, format, *args):
        pass

# --- Start the server ---
def run():
    server = HTTPServer(("", PORT), ChatHandler)
    print(f"Server running at http://localhost:{PORT}")
    print("Open that URL in your browser!")
    print("Press CTRL+C to stop.")
    server.serve_forever()

if __name__ == "__main__":
    run()