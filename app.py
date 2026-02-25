
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My CI/CD Project from MicroDegree 🚀"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}! This app is deployed using Jenkins and Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

