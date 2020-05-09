"""
schedule 定时任务
"""

import schedule


def job():
    print("I'm working...")


schedule.every().second.do(job)
