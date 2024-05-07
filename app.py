from flask import Flask, request, jsonify
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app) 

# Define character sets
characters = {
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers": "0123456789",
    "symbols": "^!$%&|[](){}:;.,*+-#@<>~",
}

# Function to generate password
def generate_password(length, options):
    static_password = ""
    for option in options:
        if option in characters:
            static_password += characters[option]
    
    random_password = ''.join(random.choice(static_password) for _ in range(int(length)))
    return random_password

@app.route('/generate-password', methods=['POST'])
def generate_password_route():
    data = request.json
    length = data.get('length')
    options = data.get('options')

    if not length or not options:
        return jsonify({'error': 'Invalid request parameters'}), 400

    password = generate_password(length, options)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
