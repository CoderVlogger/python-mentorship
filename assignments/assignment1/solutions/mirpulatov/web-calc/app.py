from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def calc():
    return render_template('calc.html')


@app.route('/', methods=['POST'])
def calc_post():
    res = request.form
    try:
        first = int(res['first'])
        second = int(res['second'])
    except ValueError as e:
        return e
    if res['action'] == 'Add':
        return str(first + second)
    elif res['action'] == 'Subtract':
        return str(first - second)
    elif res['action'] == 'Multiply':
        return str(first * second)
    elif res['action'] == 'Divide':
        if second == 0:
            return "Division by zero"
        return str(first / second)


if __name__ == '__main__':
    app.run(debug=True)
