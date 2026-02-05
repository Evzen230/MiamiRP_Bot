import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def start_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
