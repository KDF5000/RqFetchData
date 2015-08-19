# -*- coding:utf-8 -*-
__author__ = 'Defei'

from redis import Redis
from rq import Queue
from CountWord import count_words_at_url
import time

#连接redis
redis_conn = Redis(host='192.168.0.105', port=6378)
q = Queue(connection=redis_conn, async=True)  # 设置async为False则入队后会自己执行 不用调用perform

for i in range(0, 10):
    job = q.enqueue(count_words_at_url, 'http://nvie.com/')
    print job.id

# job.perform()


# r = Redis(host='127.0.0.1', port=6378)
# print r.set('test', 'hello')
# print r.get('test')