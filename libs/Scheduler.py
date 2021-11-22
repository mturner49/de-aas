'''
__author__ = 'Matt Turner'
__purpose__ = 'Schedule tasks and jobs'

'''

import time
from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler():
    def __init__(self, freq, start_time, start_day):
        self.freq = freq
        self.start_time = start_time
        self.start_day = start_day

        self.scheduler = BackgroundScheduler()

