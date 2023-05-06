from flask import Flask, request, jsonify
from flask_cors import CORS
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LinguaConsoleBot')))
from Lingua import get_language_code, get_ai_response, get_feedback

app = Flask(__name__)
CORS(app)

conversation_history = []

@app.route('/api/send-message', methods=['POST'])
def send_message():
    user_text = request.json.get('message')
    if not user_text:
        return jsonify({"error": "No message provided"}), 400

    language_code = get_language_code(user_text)
    conversation_history.append(f"User: {user_text}")
    ai_response = get_ai_response('\n'.join(conversation_history), language_code)
    conversation_history.append(f"AI: {ai_response}")

    return jsonify({"ai_response": ai_response})

@app.route('/api/request-feedback', methods=['POST'])
def request_feedback():
    language_code = request.json.get('language_code')
    if not language_code:
        return jsonify({"error": "No language code provided"}), 400

    feedback = get_feedback(conversation_history, language_code)

    return jsonify({"feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)

