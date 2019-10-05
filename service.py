from flask import Flask
from time_getter import time_getter
app = Flask(__name__)

@app.route('/')
def time_print_function():
    data = time_getter()
    str = "here is your time " + str(data)
    return str
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
