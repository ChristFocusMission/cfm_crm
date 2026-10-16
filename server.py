#!/usr/bin/env python3
"""
Christ Focus Mission - Fundraising Portal Local Server
Runs a lightweight, zero-dependency HTTP server with automatic port detection.
"""

import http.server
import socketserver
import os
import sys
import webbrowser

PORT_CANDIDATES = [8080, 8000, 5000, 3000, 8888]
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable aggressive caching for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    server = None
    selected_port = None

    for port in PORT_CANDIDATES:
        try:
            socketserver.TCPServer.allow_reuse_address = True
            server = socketserver.TCPServer(("", port), Handler)
            selected_port = port
            break
        except OSError:
            continue

    if not server:
        # Fallback to random available port
        server = socketserver.TCPServer(("", 0), Handler)
        selected_port = server.server_address[1]

    url = f"http://localhost:{selected_port}"
    print("=" * 65)
    print("  CHRIST FOCUS MISSION - FUNDRAISING LEADS PORTAL")
    print("=" * 65)
    print(f"  Server running locally at:")
    print(f"  --> {url}")
    print()
    print("  Directory: " + DIRECTORY)
    print("  Press Ctrl+C to stop the server.")
    print("=" * 65)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()
        sys.exit(0)

if __name__ == "__main__":
    run_server()
