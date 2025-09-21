from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    response = requests.get(url)
    data = response.json()
    joke_category = data['category']
    the_joke = data['joke']
    return "<h1>Welcome to My Flask API App!</h1>"


@app.route("/second_page")
def second_page():
    url = "https://v2.jokeapi.dev/joke/Programming?type=single"
    response = requests.get(url)
    data = response.json()
    joke_category = data['category']
    the_joke = data['joke']
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)