from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='Loan Calculator')

@app.route('/payment', methods=['GET', 'POST'])
def payments():
    if request.method == 'POST':
        form = request.form
        A = int(form['A'])
        n = int(form['n'])
        i = int(form['i'])
        calc = A / (((( 1 + ( i * 0.001) ) **n ) - 1 ) / ( ( i * 0.001) * ( 1 + ( i * 0.001) ) **n ))
        return render_template('index.html', display=calc, pageTitle='Loan Calculator')

    return redirect("/")


@app.route('/yinan')
def yinan():
    return render_template('yinan.html', pageTitle='About contributor')

if __name__ == '__main__':
    app.run(debug=True)
