from flask import Flask, request  # noqa

app = Flask(__name__)


@app.route('/receive', methods=['POST', 'GET', 'PUT', 'DELETE', 'PATCH'])
def receive():
    message = (
        f'{request.headers}\n\n'
        f'{request.method} {request.url}\n\n'
        f'{request.data}\n\n'
    )
    print(message)
    return message


app.run(debug=True)
