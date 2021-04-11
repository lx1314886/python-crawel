import time
from apscheduler.schedulers.blocking import BlockingScheduler
from mysql.t_shop import *
from smzdm.bcj import BcjSpider
from smzdm.jxhj import JxhjSpider
from smzdm.qbhj import QbhjSpider


def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    update_title()
def hj_job():
    BcjSpider()
    JxhjSpider()
    QbhjSpider()
def jxhj_job():
    JxhjSpider()
def qbhj_job():
    QbhjSpider()


if __name__ == '__main__':
    # 该示例代码生成了一个BlockingScheduler调度器，使用了默认的任务存储MemoryJobStore，以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。

    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用固定时间间隔（interval）的方式，每隔60分钟执行一次 minutes seconds
    # scheduler.add_job(job, 'interval',max_instances=10, minutes=60)
    scheduler.add_job(hj_job, 'interval', max_instances=10, minutes =1)
    scheduler.start()