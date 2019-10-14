#Placeholder in place

from flask import Flask
from flask_celery import make_celery
from Twitter_API import twitter_api

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost//'

celery = make_celery(app)

@app.route('/')
def counter_function():
    request = twitter_counter.delay()
    return_value = request.get()
    return return_value


@celery.task(name='twitter_api.count')
def twitter_counter():
    data = twitter_api()
    return data

if __name__ == '__main__':
    app.run('0.0.0.0')
