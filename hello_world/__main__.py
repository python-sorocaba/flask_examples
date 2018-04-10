from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '1º Grupy-SP Boituva!'


app.run(debug=True)
