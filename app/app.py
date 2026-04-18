

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._send_response(200, {"status": "ok"})
            return

        if self.path == "/":
            self._send_response(
                200,
                {
                    "message": "AWS DOP-C02 DevSecOps Lab",
                    "environment": os.getenv("APP_ENV", "dev"),
                    "service": "sample-python-app"
                }
            )
            return

        self._send_response(404, {"error": "not found"})

    def _send_response(self, status_code: int, payload: dict):
        response = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


def run():
    port = int(os.getenv("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), AppHandler)
    print(f"Server starting on port {port}")
    server.serve_forever()


if __name__ == "__main__":
    run()