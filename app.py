import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def sample():
    return f'This is the {os.environ["APP"]} application.\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0')