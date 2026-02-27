# server.py
# Pure Python web server — no Flask, no libraries!

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from chatbot import get_response  # importing your brain!

# Railway assigns a dynamic port — we must use it!
PORT = int(os.environ.get("PORT", 3000))

class ChatHandler(BaseHTTPRequestHandler):

    # --- Serve the HTML page when browser opens the URL ---
    def do_GET(self):
        if self.path == "/":
            with open("index.html", "r") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

    # --- Handle messages sent from the browser ---
    def do_POST(self):
        if self.path == "/chat":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length)
            data = json.loads(body)

            user_message = data.get("message", "")
            bot_reply = get_response(user_message)

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
    server = HTTPServer(("0.0.0.0", PORT), ChatHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()