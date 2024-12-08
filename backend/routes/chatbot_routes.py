from flask import Blueprint, request, jsonify
from utils.dataset_loader import load_dataset
from utils.nlp import match_intent
from database.db_config import get_connection

chatbot_bp = Blueprint('chatbot', __name__)

dataset = load_dataset('Conversation.csv')

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get('query', '')
    token = data.get('token', '')

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        response = match_intent(user_query, dataset)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO responses (query, response, token) VALUES (%s, %s, %s)",
            (user_query, response, token)
        )
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"response": response}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
