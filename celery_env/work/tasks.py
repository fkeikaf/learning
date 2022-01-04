from celery import Celery

app = Celery(
    'tasks',
    backend='db+postgresql://postgres:postgres@172.30.147.225:5432/sampledb',
    broker='amqp://guest:guest@172.30.147.225//'
)


@app.task
def add(x, y):
    return x + y
