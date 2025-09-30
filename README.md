# Hello World CI/CD Learning Project

This is a simple Python project designed to learn CI/CD concepts using GitHub Actions.

## Project Structure

- `hello.py` - Main application with a simple greeting function
- `test_hello.py` - Unit tests for the application
- `requirements.txt` - Python dependencies (currently empty)
- `.github/workflows/` - GitHub Actions CI/CD workflows

## Running Locally

```bash
# Run the application
python hello.py

# Run tests
python -m pytest test_hello.py
# or
python test_hello.py
```

## CI/CD Features

This project demonstrates:
- Automated testing on every code change
- Code quality checks
- Build verification
- Deployment readiness (foundation for future expansion)

## Learning Objectives

- Understanding CI/CD concepts
- GitHub Actions workflow creation
- Automated testing
- Version control best practices
