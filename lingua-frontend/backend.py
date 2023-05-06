from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LinguaConsoleBot')))
from Lingua import get_language_code, get_feedback, get_ai_response # Import the Lingua.py module

app = Flask(__name__)

@app.route('/lingua', methods=['POST'])
def lingua():
    # Extract data from the JSON payload
    data = request.get_json()
    user_text = data.get('user_text')

    # Call Lingua.py functions to get the language code and AI response
    language_code = get_language_code(user_text)
    ai_response = get_ai_response(user_text, language_code)

    # Return the AI response as JSON
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)