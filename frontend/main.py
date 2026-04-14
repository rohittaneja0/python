# frontend/app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    API = os.getenv("API")
    return render_template("index.html", API=API)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
