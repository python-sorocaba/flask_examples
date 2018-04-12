from flask import Flask, request  # noqa

app = Flask(__name__)


@app.route('/sum_numbers/<int:a>/<int:b>/', methods=['GET'])
def sum_numbers(a, b):
    total = a + b
    return str(total)


app.run(debug=True)
