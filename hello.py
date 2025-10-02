#!/usr/bin/env python3
"""
Flask Hello World application for learning CI/CD
"""

from flask import Flask, jsonify
import os


def say_hello(name="World"):
    """Return a greeting message"""
    return f"Hello, {name}!"


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
        "status": "success"
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
    """API information"""
    return jsonify({
        "name": "Hello CI/CD API",
        "version": "1.0.0",
        "description": "A simple Flask API for learning CI/CD",
        "endpoints": [
            "/",
            "/hello",
            "/hello/<name>",
            "/health",
            "/api/info"
        ]
    })


if __name__ == "__main__":
    # Get port from environment variable or default to 8000
    port = int(os.environ.get('PORT', 8000))

    # Run the Flask app
    app.run(
        host='0.0.0.0',  # Allow external connections
        port=port,
        debug=False  # Set to False for production
    )
