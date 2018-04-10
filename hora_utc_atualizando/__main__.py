from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/time_now', methods=['GET'])
def time_now():
    utc_time = datetime.utcnow().time()
    localized_time = datetime.now().time()
    return render_template(
        'time.html',
        utc_time=utc_time,
        localized_time=localized_time,
    )


app.run(debug=True)
