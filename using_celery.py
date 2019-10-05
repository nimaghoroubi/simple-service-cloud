from celery import Celery

app = Celery('using_celery', broker='pyamqp://guest@localhost//')

@app.task
def add(x,y):
    return x + y
