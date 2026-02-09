from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app) # Allows frontend to talk to backend

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency.",
    "Make it work, make it right, make it fast.",
    "Talk is cheap. Show me the code."
]

@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify({'quote': random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
