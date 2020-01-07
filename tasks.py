from celery import Celery 

app = Celery('webscraper', broker='pyamqp://localhost//')

@app.task
def game_text(myMessage):
    print(myMessage)