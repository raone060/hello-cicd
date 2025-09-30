#!/usr/bin/env python3
"""
Simple Hello World application for learning CI/CD
"""

def say_hello(name="World"):
    """Return a greeting message"""
    return f"Hello, {name}!"

def main():
    """Main function to run the application"""
    print(say_hello())
    print(say_hello("DevOps Learner"))

if __name__ == "__main__":
    main()
