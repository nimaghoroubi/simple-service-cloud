#first try to merge celery and flask

from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost//'

celery = make_celery(app)

@app.route('/<name>')
def time_print_function(name):
    reverse.delay(name)

    return 'request successful'


@celery.task(name='service.reverse')
def reverse(string):
    return string[::-1]

if __name__ == '__main__':
    app.run('0.0.0.0')
