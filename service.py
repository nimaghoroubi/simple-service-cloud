#returns server time with time_getter

from flask import Flask
import subprocess
from time_getter import time_getter


app = Flask(__name__)

@app.route('/')
def time_print_function():
    data = time_getter()
    data = "your time is " + str(data) + "\n"
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
