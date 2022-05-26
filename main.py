from flask import Flask, request
from calculator import Calculator

calc = Calculator()

application = Flask(__name__)

@application.route('/')
def home():
    return 'azure flask calc'

@application.route('/add')
def add_f():
    return str(calc.add(request.args.get('x'), request.args.get('y')))

@application.route('/mult')
def mult_f():
    return str(calc.mult(request.args.get('x'), request.args.get('y')))


if __name__ == '__main__':
    application.run()