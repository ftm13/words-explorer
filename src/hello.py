from flask import Flask, jsonify
from flask_cors import CORS
from queries import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def greet():
    return "Good to see you! Navigate to /context/我"

@app.route('/context/<word>')
def get_word_bigrams(word):
    response = jsonify(getBigramContext(word,10))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')