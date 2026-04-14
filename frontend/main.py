# frontend/app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    API= os.getenv("API", "http://127.0.0.1:5001")
    return render_template("index.html", API=API)

if __name__ == "__main__":
    app.run(port=5000, debug=True)