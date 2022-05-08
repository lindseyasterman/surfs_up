from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route("/about")
def about():
    name = "Lindsey"
    location = "Holly Springs"

    return f"My name is {name}, and I live in {location}."
