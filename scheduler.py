import tkFont
from Tkinter import *
from schedule import *
from appointment import *

class Scheduler:
    def __init__(self, root, schedule):
        self.root = root
        self.schedule = schedule
        self.days, self.tvs = [], []
        self.appointments = []
        self.add_menu_bar() # add menu bar
        self.add_header() # add top buttons and month label to frame
        self.frame = Frame(self.root)
        self.frame.pack()
        self.add_days() # adds calendar to frame
        # sets the selected day to today
        for i, date in enumerate(self.schedule.get_calendar()):
            if date.month == self.schedule.date.month and date.day == self.schedule.date.day:
                self.selected_day = self.days[i]
                self.selected_day.config(foreground="WHITE", background="BLUE")
        self.add_appointments() # add appointment frame

    def add_menu_bar(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="New", command=self.new_note)
        file_menu.add_command(label="Open", command=self.open_note)
        menu.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu)

    def add_header(self):
        frame = Frame(self.root, padx=15, pady=15)
        frame.pack()
        Button(frame, text="<", command=lambda x = False:self.change_month(x)).grid(row=0, column=0)
        self.month_lbl = Label(frame, padx=15, text=self.schedule.date.strftime("%B %Y"))
        self.month_lbl.grid(row=0, column=1)
        Button(frame, text=">", command=lambda x = True:self.change_month(x)).grid(row=0, column=2)
        frame = Frame(self.root)
        frame.pack()
        days_of_week = ("M", "T", "W", "R", "F", "S", "S")
        for i, day in enumerate(days_of_week):
            Label(frame, text=day, width=3).grid(row=0, column=i)

    def add_days(self):
        self.selected_day = None
    	for day in self.days:
    	    day.destroy()
        self.tvs, self.days = [], []
        for i, date in enumerate(self.schedule.get_calendar()): # add calendar
            tv = IntVar()
            tv.set(date.day)
            self.tvs.append(tv)
            self.days.append(Label(self.frame, bg="white", width=3, textvariable=tv))
            self.days[-1].grid(row=(i / 7), column=(i % 7))
            if date.month != self.schedule.date.month:
            	self.days[-1].configure(state=DISABLED)
            else:
                self.days[-1].bind("<Button-1>", self.select_day)
                self.days[-1].bind("<Double-Button-1>", self.new_note)

    def add_appointments(self):
        frame = Frame(self.root)
        frame.pack(anchor=W)
        appointment_lbl = Label(frame, text="Appointments", pady=15)
        appointment_lbl.pack()
        f = tkFont.Font(appointment_lbl, appointment_lbl.cget("font"))
        f.configure(underline=True)
        appointment_lbl.configure(font=f)
        self.appointment_list = Listbox()
        self.appointment_list.pack()
        self.appointment_list.bind("<Double-Button-1>", self.open_note)
        self.change_appointments()

    def select_day(self, arg):
        if self.selected_day is not None:
            self.selected_day.config(foreground="BLACK", background="WHITE")
        self.selected_day = arg.widget
        self.selected_day.config(foreground="WHITE", background="BLUE")
        for i, day in enumerate(self.days):
            if self.selected_day == day:
                self.schedule.change_day(self.tvs[i].get())

    def change_month(self, is_next):
        if is_next:
            self.schedule.next_month()
        else:
            self.schedule.prev_month()
        self.add_days()
        self.month_lbl.configure(text=self.schedule.date.strftime("%B %Y"))
        self.change_appointments()
        
    def change_appointments(self):
        self.appointment_list.delete(0, END)
        self.appointments = get_appointments(self.schedule.date.month)
        for appointment in self.appointments:
            self.appointment_list.insert(END, appointment["date"].strftime("%d/%m/%Y %H:%M"))

    def open_note(self, arg=None):
        appointment = self.appointments[int(self.appointment_list.curselection()[0])]
        Appointment(appointment["date"], appointment["message"], scheduler=self, id=appointment["id"])

    def new_note(self, *args, **kwargs):
        Appointment(self.schedule.date, scheduler=self)

root = Tk()
scheduler = Scheduler(root, Schedule())
root.mainloop()