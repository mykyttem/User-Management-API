from flask import jsonify
from dotenv import load_dotenv
from app import create_app

load_dotenv()

app = create_app()

@app.route("/")
def home():
    return jsonify({"message": "Hello world"})