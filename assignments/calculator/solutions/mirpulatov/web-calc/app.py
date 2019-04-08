from flask import Flask, render_template, request
from calc import Calculator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calc.html')

@app.route('/', methods=['POST'])
def home_post():
    res = request.form
    try:
        first = int(res['first'])
        second = int(res['second'])
    except ValueError as e:
        return e
    calc = Calculator(first, second)
    try:
        if res['action'] == 'Add':
            return 'Result: {}'.format(calc.plus())
        elif res['action'] == 'Subtract':
            return 'Result: {}'.format(calc.minus())
        elif res['action'] == 'Multiply':
            return 'Result: {}'.format(calc.multiply())
        elif res['action'] == 'Divide':
            return 'Result: {}'.format(calc.div())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)
