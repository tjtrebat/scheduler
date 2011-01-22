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

    def days_in_month(self):
        return calendar.monthrange(self.date["year"], self.date["month"])[1]

    def prev_month(self):
    	if self.date["month"] <= 1:
    		self.date["year"] -= 1
    		self.date["month"] = 12
    	else:
    		self.date["month"] -= 1

    def next_month(self):
    	if self.date["month"] >= 12:
    		self.date["year"] += 1
    		self.date["month"] = 1
    	else:
    		self.date["month"] += 1

    def get_full_lbl(self):
        return "%s %s, %s" % (calendar.month_name[self.date["month"]], self.date["day"], self.date["year"])

    def get_month_lbl(self):
        return "%s %s" % (calendar.month_name[self.date["month"]], self.date["year"])

    def get_calendar(self):
        return self.calendar.itermonthdates(self.date["year"], self.date["month"])