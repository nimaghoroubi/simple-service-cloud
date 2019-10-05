from celery import celery

app = Celery('using_celery', broker='pyamqp://ubuntu@localhost//')

@app.task
def add(x,y):
    return x + y
