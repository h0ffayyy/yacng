from flask import Flask
from flask import render_template
from flask import jsonify
import random
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/generate_codename')
def generate_codename():
    wordlist_dir = "static/wordlists/"
    wordlists = []

    for filename in os.listdir(wordlist_dir):
        wordlists.append(filename)

    wordlist = random.choice(wordlists)

    lines = open(wordlist_dir+wordlist).read().splitlines()
    line = random.choice(lines)

    return jsonify({'codename' : line})