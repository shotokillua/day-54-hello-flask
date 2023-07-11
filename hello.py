from flask import Flask

app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrappper_function():
        return '<b>' + function() + '</b>'
    return wrappper_function

def make_emphasis(function):
    def wrapper_function():
        return '<em>' + function() + '</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return '<u>' + function() + '</u>'
    return wrapper_function

@app.route('/')  # The '/' navigates you to the home page  # The @ sign signifies that it is a decorator that is giving extra functionality to the hello_world function
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph. Hook Em Baby! \m/</p>' \
           '<iframe src="https://giphy.com/embed/Rk8BFcAo13Zd5cpsDJ"</iframe> width=100'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)