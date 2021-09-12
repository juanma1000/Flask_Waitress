from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!, Sorpesa'


if __name__ == '__main__':
    #app.run()
    serve(app, host='0.0.0.0', port=5000)
