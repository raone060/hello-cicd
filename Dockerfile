# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY hello.py .
COPY test_hello.py .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Expose port for Flask web service
EXPOSE 8080

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=hello.py
ENV FLASK_ENV=development

# Health check for Flask app
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Run the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "hello:app"]