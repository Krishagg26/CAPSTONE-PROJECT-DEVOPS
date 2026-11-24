import http.server, socketserver, json, os, time, hashlib

START_TIME = time.time()
REQUEST_COUNT = 0
VERSION = os.getenv("APP_VERSION", "v1.0")
SECRET_TOKEN = os.getenv("VAULT_API_SECRET", "default-dev-token")

class DevOpsHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        log_entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ"), "level": "INFO", "version": VERSION, "path": self.path, "secret_masked": "***MASKED***"}
        print(json.dumps(log_entry), flush=True)

    def do_GET(self):
        global REQUEST_COUNT
        REQUEST_COUNT += 1
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy", "version": VERSION}).encode())
        elif self.path == "/metrics":
            uptime = round(time.time() - START_TIME, 2)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            metrics = f"# TYPE http_requests_total counter\nhttp_requests_total {REQUEST_COUNT}\n# TYPE app_uptime_seconds gauge\napp_uptime_seconds {uptime}\n"
            self.wfile.write(metrics.encode())
        else:
            digest = hashlib.sha256(SECRET_TOKEN.encode()).hexdigest()[:12]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"service": "KRMU-Pulse-Capstone", "version": VERSION, "auth_fingerprint": digest}).encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", 8080), DevOpsHandler) as httpd:
        print(json.dumps({"event": "server_started", "port": 8080, "version": VERSION}), flush=True)
        httpd.serve_forever()
