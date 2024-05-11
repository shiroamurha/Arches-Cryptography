from flask import Flask, render_template, request, redirect
from arches import Arches
from os import system as sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET','POST'])
def encode():
    if request.method == 'POST':
        print(str(request.form.get('input')))
    return redirect('/')

@app.route('/decode', methods=['GET','POST'])
def decode():
    if request.method == 'POST':
        print(str(request.form.get('input')))
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)