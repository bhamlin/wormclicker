#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return 'Test 3!'
