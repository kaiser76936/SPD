from flask import Flask
from flask import request

app = Flask('Simple App')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.json:
            return 'Got a POST request with a body: %s' % str(request.json)
        else:
            return 'Got a POST request without a body!'
    else:
        return 'index function from a GET request'