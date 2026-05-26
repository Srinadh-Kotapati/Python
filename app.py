from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args['name']
        return f'{greeting}, {name}'
    else:
        return "some arguments are missing"


@app.route( '/hello', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'requested for GET method'
    elif request.method == 'POST':
        return 'requested for POST method'
    else:
        return 'You will never see this'

@app.route('/greet/<name>')
def greet(name):
    return f"Hey Haii {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f"{num1}+{num2} = {num1 + num2}"

if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug= True)