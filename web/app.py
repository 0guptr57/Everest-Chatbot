import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request, jsonify
import json
from chatbot.chatbot_utils import predict_class, get_response


app = Flask(__name__)

# Load intents
INTENTS_PATH = os.path.join(os.path.dirname(__file__), "..", "chatbot", "intents.json")
with open(INTENTS_PATH) as f:
    intents_data = json.load(f)

# Group intents and patterns for sidebar
sidebar_data = [
    {"tag": intent["tag"], "patterns": intent["patterns"][:3]}
    for intent in intents_data["intents"]
]


@app.route("/")
def index():
    return render_template("index.html", sidebar=sidebar_data)


@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")
    intent = predict_class(message)
    response = get_response(intent)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
