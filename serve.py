"""Serveur local : python serve.py  ->  http://localhost:8000 (le PWA marche sur localhost)."""
import http.server, socketserver, webbrowser
PORT = 8000
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as s:
    print(f"TalcoTime sur http://localhost:{PORT}  (Ctrl+C pour arrêter)")
    webbrowser.open(f"http://localhost:{PORT}")
    s.serve_forever()
