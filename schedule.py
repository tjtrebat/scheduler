__author__ = 'Tom'

import calendar
import datetime

class Schedule:
    def __init__(self, *args, **kwargs):
        today = datetime.datetime.today()
        self.calendar = calendar.Calendar()
        self.date = map(lambda x, y: x or y, args, (today.day, today.month, today.year))
        self.date = {"day": self.date[0] or today.day,
                     "month": self.date[1] or today.month,
                     "year": self.date[2] or today.year}
        for arg, val in kwargs.items():
            self.date[arg] = val
        self.date = datetime.datetime(**self.date)

    def get_calendar(self):
        return self.calendar.itermonthdates(self.date.year, self.date.month)

    def days_in_month(self, year=None, month=None):
        if year is None or month is None:
            return calendar.monthrange(self.date.year, self.date.month)[1]
        else:
            return calendar.monthrange(year, month)[1]

    def change_day(self, day):
        self.date = datetime.datetime(self.date.year, self.date.month, day)

    def prev_month(self):
    	if self.date.month <= 1:
            self.date = datetime.datetime(self.date.year - 1, 12,
                                      self.days_in_month(year=self.date.year - 1, month=12))
    	else:
    		self.date = datetime.datetime(self.date.year, self.date.month - 1,
                                      self.days_in_month(year=self.date.year, month=self.date.month - 1))

    def next_month(self):
    	if self.date.month >= 12:
            self.date = datetime.datetime(self.date.year + 1, 1, 1)
    	else:
    		self.date = datetime.datetime(self.date.year, self.date.month + 1, 1)