#!/usr/bin/env python3
"""
Flask Hello World application for learning CI/CD
"""

from flask import Flask, jsonify, request
import os
import socket


def say_hello(name="World"):
    """Return a greeting message"""
    return f"Hello, {name}!"


def get_host_info():
    """Get host IP and hostname information"""
    try:
        # Get hostname
        hostname = socket.gethostname()

        # Get local IP address
        local_ip = socket.gethostbyname(hostname)

        # Get external IP (if available)
        external_ip = None
        try:
            # This might not work in all environments
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            external_ip = s.getsockname()[0]
            s.close()
        except Exception as e:
            print(f"Error getting external IP: {e}")
            pass

        return {
            "hostname": hostname,
            "local_ip": local_ip,
            "external_ip": external_ip
        }
    except Exception as e:
        return {
            "hostname": "unknown",
            "local_ip": "unknown",
            "external_ip": "unknown",
            "error": str(e)
        }


# Create Flask application
app = Flask(__name__)


@app.route('/')
def home():
    """Home page"""
    return jsonify({
        "message": say_hello(),
        "status": "success",
        "service": "Hello CI/CD Flask App"
    })


@app.route('/hello')
def hello():
    """Hello endpoint"""
    return jsonify({
        "message": say_hello(),
        "status": "success",
        "name": "Charulochana"
    })


@app.route('/hello/<name>')
def hello_name(name):
    """Hello with custom name"""
    return jsonify({
        "message": say_hello(name),
        "status": "success"
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "hello-cicd",
        "version": "1.0.0"
    })


@app.route('/api/info')
def api_info():
    """API information with host details"""
    host_info = get_host_info()

    return jsonify({
        "name": "Hello CI/CD API",
        "version": "1.0.0",
        "description": "A simple Flask API for learning CI/CD",
        "host_info": host_info,
        "request_info": {
            "remote_addr": request.remote_addr,
            "user_agent": request.headers.get('User-Agent', 'Unknown'),
            "host": request.headers.get('Host', 'Unknown')
        },
        "endpoints": [
            "/",
            "/hello",
            "/hello/<name>",
            "/health",
            "/api/info"
        ]
    })


if __name__ == "__main__":
    # Get port from environment variable or default to 8080
    port = int(os.environ.get('PORT', 8080))

    # Run the Flask app
    app.run(
        host='0.0.0.0',  # Allow external connections
        port=port,
        debug=False  # Set to False for production
    )
