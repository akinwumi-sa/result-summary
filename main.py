from flask import Flask, render_template
import json

app = Flask(__name__)

with open('data.json', 'r') as file:
    data = json.load(file)


@app.route('/')
def home():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
