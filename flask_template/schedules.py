"""
schedule 定时任务
"""

import schedule
from flask import current_app


def job():
    current_app.logger.info("I'm working...")


schedule.every().second.do(job)
