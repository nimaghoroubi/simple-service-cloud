from celery import Celery
from twitter_api import twitter_api

app = Celery('tweetsApp',
             backend='rpc://',
             broker='pyamqp://tweets:tweets@192.168.1.26/tweets')

# Do tasks here
