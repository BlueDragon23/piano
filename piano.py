from flask import Flask
from flask import render_template
import string

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', string=string)


if __name__ == '__main__':
    app.run()
