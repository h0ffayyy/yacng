from flask import Flask
from flask import render_template
from flask import jsonify
import random

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/generate_codename')
def generate_codename():
    file1 = "static/wordlists/city_names.txt"

    lines = open(file1).read().splitlines()
    line =random.choice(lines)
    return jsonify({'codename' : line})