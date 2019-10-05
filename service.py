#Placeholder in place

from flask import Flask
from flask_celery import make_celery
from count_api import count_API

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost//'

celery = make_celery(app)

@app.route('/')
def counter_function():
    count_implementation.delay()
    return "job queued"


@celery.task(name='service.count')
def count_implementation():
    data = count_API()
    return data

if __name__ == '__main__':
    app.run('0.0.0.0')
