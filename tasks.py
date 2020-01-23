from celery import Celery 
from webscraper import main

app = Celery('webscraper', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def game_text():
    main()