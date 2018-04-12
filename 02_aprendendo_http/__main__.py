from flask import Flask, request  # noqa

app = Flask(__name__)


@app.route('/receive', methods=['POST', 'GET', 'PUT', 'DELETE', 'PATCH'])
def receive():
    message = (
        '-----------------\n'
        f'Headers: \n{request.headers}\n\n'
        f'Method: \n{request.method}\n\n'
        f'URL: \n{request.url}\n\n'
        f'Body: \n{request.data}\n'
        '-----------------'
    )
    print(message)
    return message


app.run(debug=True)
