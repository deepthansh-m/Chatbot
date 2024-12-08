from flask import Flask
from routes.chatbot_routes import chatbot_bp
from database.db_setup import setup_database
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(chatbot_bp, url_prefix='/api')

setup_database()

if __name__ == "__main__":
    app.run(debug=True)
