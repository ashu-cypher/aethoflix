#!/usr/bin/env python3
"""
AethoFlix LAN server — run this on your PC, open the printed address
in your TV's web browser (TV must be on the same Wi-Fi).

Usage:
    python3 serve.py            # serves on port 8000
    python3 serve.py 9000       # custom port
"""
import http.server
import socket
import sys
from functools import partial

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


handler = partial(http.server.SimpleHTTPRequestHandler)
httpd = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), handler)

print("=" * 52)
print("  AethoFlix is serving this folder on your home network")
print("=" * 52)
print(f"  On your TV's browser, open:\n")
print(f"      http://{lan_ip()}:{PORT}/\n")
print("  (TV and this PC must be on the same Wi-Fi.)")
print("  Press Ctrl+C to stop.")
print("=" * 52)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nStopped.")
