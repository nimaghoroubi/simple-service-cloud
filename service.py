from flask import Flask
from time_getter import time_getter
app = Flask(__name__)

@app.route('/')
def start_text():
    return "hello user, lets start with time"
def time_print_function():
    return time_getter.time_getter()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
