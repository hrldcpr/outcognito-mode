import flask
import flask_cors

import api

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/tweet', methods=['POST'])
def tweet():
    api.post('statuses/update', status=flask.request.values['status'])
    return 'ok'

app.run(host='0.0.0.0', debug=True)
