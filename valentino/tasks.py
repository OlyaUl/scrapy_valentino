from celery import Celery
from celery.task import Task
#from pymongo import MongoClient

from .items import ValentinoProduct, ValentinoPrice

app = Celery(broker= 'redis://localhost:6379/0')
#app = Celery(broker='amqp://admin:admin@localhost:15672//')


import sys
import psycopg2

HOST    = 'localhost'
DB_NAME = 'val'
DB_USER = 'postgres'
DB_PASS = '1'

@app.task(name="save")
def save(item):
    #  print(item)
    # f = open('test.txt', 'w')
    # f.write((item))

    conn = psycopg2.connect(host=HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    curs = conn.cursor()

    curs.execute("""INSERT INTO "Product" VALUES (%s)""" % item)
    conn.commit()

    curs.close()
    conn.close()


if __name__ == '__main__':
    app.worker_main()