from flask import Flask
app = Flask(__name__)

import demo.service

@app.route("/")
def welcome():
    return "<p>Welcome to the Python Docker demo!</p>"