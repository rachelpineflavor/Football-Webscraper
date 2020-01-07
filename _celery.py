from celery import Celery
from celery.schedules import crontab

#sudo rabbitmqctl add_user RachelCardwell rachymeister
#sudo rabbitmqctl add_vhost sample_host
#sudo rabbitmqctl set_user_tags RachelCardwell administrator
#sudo rabbitmqctl set_permissions -p sample_host RachelCardwell ".*" ".*" ".*"

#app = Celery('webscraper', backend='rpc://', broker='pyamqp://RachelCardwell:rachymeister@localhost:5672/sample_host')

app = Celery('webscraper', broker='pyamqp://localhost//')

app.conf.beat_schedule = {
    # Executes every Thursday morning at 10:30 a.m.
    'add-every-Thursday-morning': {
        'task': 'task.add',
        'schedule': crontab(hour=8, minute=25, day_of_week=5),
        'args': (16, 16),
    },
}