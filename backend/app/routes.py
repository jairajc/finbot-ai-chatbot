from flask import Blueprint, request, jsonify
from .utils import ask_openai

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to FinBot API'})

@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "Missing 'message' in request"}), 400

    response = ask_openai(user_input)
    return jsonify({"response": response})
