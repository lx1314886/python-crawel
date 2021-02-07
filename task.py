import time
from apscheduler.schedulers.blocking import BlockingScheduler
from mysql.t_shop import *
def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    update_title()


if __name__ == '__main__':
    # 该示例代码生成了一个BlockingScheduler调度器，使用了默认的任务存储MemoryJobStore，以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。

    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式

    # 采用固定时间间隔（interval）的方式，每隔60分钟执行一次 minutes
    scheduler.add_job(job, 'interval', minutes=60)
    scheduler.start()