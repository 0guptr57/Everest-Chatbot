# chatbot/chatbot_utils.py

import random
import json
import pickle
import numpy as np
import os
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# Directories
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")
CHATBOT_DIR = os.path.join(BASE_DIR, "chatbot")

# Load assets
lemmatizer = WordNetLemmatizer()
intents = json.loads(open(os.path.join(CHATBOT_DIR, "intents.json")).read())
words = pickle.load(open(os.path.join(MODEL_DIR, "words.pkl"), "rb"))
classes = pickle.load(open(os.path.join(MODEL_DIR, "classes.pkl"), "rb"))
model = load_model(os.path.join(MODEL_DIR, "chatbot_model.keras"))


def clean_up_sentence(sentence):
    sentence_words = sentence.split()
    return [lemmatizer.lemmatize(word.lower()) for word in sentence_words]


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [1 if word in sentence_words else 0 for word in words]
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    top_index = np.argmax(res)
    top_prob = res[top_index]
    threshold = 0.75
    if top_prob < threshold:
        return "fallback"
    return classes[top_index]


def get_response(intent):
    for item in intents["intents"]:
        if item["tag"] == intent:
            return random.choice(item["responses"])
    return "I'm not sure how to help with that."
