#!/usr/bin/python3

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    """defines the hello function"""
    name = request.args.get("name", "World")
    return (f"Hello {escape(name)}!")

if __name__ == "__main__":
    hello()
print("\nCode developed by Masino")
