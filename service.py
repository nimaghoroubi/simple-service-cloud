#first try to merge celery and flask

from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost//'

celery = make_celery(app)

@app.route('/')
def time_print_function():
    reverse.delay('item_test')

    return 'request successful'


@celery.task(name='service.reverse')
def reverse(string):
    return string[::-1]

if __name__ == '__main__':
    app.run('0.0.0.0')
