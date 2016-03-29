# -*- coding: utf-8 -*-
__author__ = 'Hipeace86'
__datetime__ = '15-8-18'
"""
Celery Tasks
"""
import os
import time
from celery import Celery

celery = Celery("tasks", broker="amqp://")
celery.conf.CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'amqp')


@celery.task
def AppendMinion(name):
    # TODO: 生成配置文件
    # TODO: 拷贝镜像
    # TODO: 启动虚拟机
    time.sleep(10)
    return name


if __name__ == "__main__":
    AppendMinion.delay('AppendMinion')
