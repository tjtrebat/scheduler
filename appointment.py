__author__ = 'Tom'

import calendar
from Tkinter import *

class Appointment:
    def __init__(self, date):
        self.frame = Frame(Tk(), padx=10, pady=10)
        self.frame.pack()
        self.date = date
        self.add_date() # add date
        self.add_time() # add time
        self.add_message() # add message box

    def add_date(self):
        date = Frame(self.frame)
        Label(date, text="Date").grid(row=0, column=0)
        self.days = self.get_spin_box(date, self.date.day, width=2, from_=1,
                          to=calendar.monthrange(self.date.year, self.date.month)[1])
        self.days.grid(row=0, column=1)
        Label(date, text="/").grid(row=0, column=2)
        self.months = self.get_spin_box(date, self.date.day, width=2, from_=1, to=12)
        self.months.config(command=self.change_days)
        self.months.grid(row=0, column=3)
        Label(date, text="/").grid(row=0, column=4)
        self.years = self.get_spin_box(date, self.date.year, width=4, from_=1, to=9999)
        self.years.config(command=self.change_days)
        self.years.grid(row=0, column=5)
        date.grid(sticky="w")

    def add_time(self):
        time = Frame(self.frame)
        Label(time, text="Time").grid(row=0, column=0)
        self.hours = self.get_spin_box(time, self.date.hour % 12, width=2, from_=1, to=12)
        self.hours.grid(row=0, column=1) # add hours
        Label(time, text=":").grid(row=0, column=2)
        self.minutes = self.get_spin_box(time, self.date.minute, width=2, values=tuple(str(i).zfill(2) for i in range(60)))
        self.minutes.grid(row=0, column=3) # add minutes
        am_pm = StringVar(time)
        if self.date.hour < 12:
            am_pm.set("am")
        else:
            am_pm.set("pm")
        w = OptionMenu(time, am_pm, "am", "pm") # add am/pm
        w.grid(row=0, column=4)
        time.grid(sticky="w")

    def get_spin_box(self, frame, selected, **kwargs):
        spin_box = Spinbox(frame)
        spin_box.config(**kwargs)
        [spin_box.invoke('buttonup') for i in range(selected - 1)]
        return spin_box

    def add_message(self):
        f = Frame(self.frame)
        f.grid()
        Label(f, text="Message:").pack(anchor="w")
        scroll_bar = Scrollbar(f)
        text = Text(f, width=30, height=5, yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=text.yview)
        scroll_bar.pack(side='right', fill='y')
        text.pack(side='left', expand=0, fill='both')
        Button(self.frame, text="Save", padx=10, command=self.save_note).grid(pady=10)

    def change_days(self):
        self.days.config(from_=1, to=calendar.monthrange(int(self.years.get()), int(self.months.get()))[1])

    def save_note(self, *args, **kwargs):
    	print kwargs