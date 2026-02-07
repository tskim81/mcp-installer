#!/usr/bin/env python3
import sys
import json
import urllib.request
import urllib.error
import os
import signal

# Configuration
URL = "https://stitch.googleapis.com/mcp"
API_KEY = "AQ.Ab8RN6J-iXNkA-Hy070K72VD9qxM3XR4iLsFE9yuC4lF-wPJDg"
LOG_FILE = "/Users/tskim/.gemini/antigravity/stitch_proxy.log"
TIMEOUT = 30  # seconds

def log(msg):
    """Log to file for debugging."""
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[StitchProxy] {msg}\n")
    except:
        pass

def handle_sigint(signum, frame):
    log("Received SIGINT, exiting.")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def main():
    log("Starting Stitch Proxy for Antigravity (v2)...")
    
    while True:
        try:
            # specifically use sys.stdin (text mode) since JSON-RPC is text
            line = sys.stdin.readline()
            if not line:
                break
            
            line = line.strip()
            if not line:
                continue

            try:
                request = json.loads(line)
            except json.JSONDecodeError:
                log(f"Invalid JSON received: {line[:50]}...")
                continue

            # Prepare request
            headers = {
                "Content-Type": "application/json",
                "X-Goog-Api-Key": API_KEY,
                "Accept": "application/json"
            }
            
            data = json.dumps(request).encode('utf-8')
            req = urllib.request.Request(URL, data=data, headers=headers, method='POST')

            try:
                with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                    resp_data = resp.read()
                    sys.stdout.buffer.write(resp_data)
                    sys.stdout.buffer.write(b"\n")
                    sys.stdout.flush()
                    
            except urllib.error.HTTPError as e:
                err_body = e.read()
                log(f"HTTP Error {e.code}: {e.reason}")
                
                # Check if it's a JSON-RPC error response from server
                try:
                    if err_body:
                        json.loads(err_body) # validate
                        sys.stdout.buffer.write(err_body)
                        sys.stdout.buffer.write(b"\n")
                        sys.stdout.flush()
                    else:
                        raise ValueError("Empty error body")
                except:
                    # Construct manual error
                    err_msg = {
                        "jsonrpc": "2.0",
                        "error": {
                            "code": -32000, 
                            "message": f"HTTP Error {e.code}: {e.reason}"
                        },
                        "id": request.get("id")
                    }
                    sys.stdout.write(json.dumps(err_msg) + "\n")
                    sys.stdout.flush()

            except Exception as e:
                log(f"Request Error: {e}")
                if request.get("id") is not None:
                    err_msg = {
                        "jsonrpc": "2.0",
                        "error": {
                            "code": -32603,
                            "message": f"Proxy Error: {str(e)}"
                        },
                        "id": request.get("id")
                    }
                    sys.stdout.write(json.dumps(err_msg) + "\n")
                    sys.stdout.flush()

        except Exception as e:
            log(f"Loop Error: {e}")
            break

if __name__ == "__main__":
    main()
