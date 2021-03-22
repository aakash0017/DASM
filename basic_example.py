__author__ = 'kai'

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']

name=hello().first_name

def return_name(name):
	return name

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)