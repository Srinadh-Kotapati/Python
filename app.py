from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello world</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"Hey Haii {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f"{num1}+{num2} = {num1 + num2}"

if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug= True)