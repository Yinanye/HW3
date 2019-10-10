from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Loan Calculator')

@app.route('/yinan')
def yinan():
    return render_template('yinan.html', pageTitle='About contributor')

if __name__ == '__main__':
    app.run(debug=True)
