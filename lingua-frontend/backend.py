from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LinguaConsoleBot')))
from Lingua import get_language_code, get_feedback, get_ai_response # Import the Lingua.py module

app = Flask(__name__)
CORS(app)

@app.route('/api/send-message', methods=['POST'])
def lingua():
    user_text = request.json['message']
    print("Request JSON:", request.json)  # Add this line to print the request data
    language_code = get_language_code(user_text)
    return jsonify({"language_code": language_code})


if __name__ == '__main__':
    app.run(debug=True)