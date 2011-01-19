import calendar
import datetime
import tkFont
from Tkinter import *

class Scheduler:
    def __init__(self, root):
        frame = Frame(root, padx=15, pady=15)
        frame.pack()
        self.c = calendar.Calendar() 
        today = datetime.datetime.now()
        self.month, self.year, self.day = today.month, today.year, today.day
        self.num_selected_day = self.day
        Button(frame, text="<", command=self.prev_month).grid(row=0, column=0)
        self.month_lbl = Label(frame, padx=15, text=today.strftime("%B %Y"))
        self.month_lbl.grid(row=0, column=1)
        Button(frame, text=">", command=self.next_month).grid(row=0, column=2)
        self.frame = Frame(root)
        self.frame.pack()
        self.days = []
        self.tvs = []
        self.add_days()
        frame = Frame(root)
        frame.pack(anchor=W)
        Label(frame, text="Today: " + today.strftime("%m-%d-%y")).pack() 
        appt_lbl = Label(frame, text="Appointments", pady=15)
        appt_lbl.pack()
        f = tkFont.Font(appt_lbl, appt_lbl.cget("font"))
        f.configure(underline=True)
        appt_lbl.configure(font=f)
        self.appt_list = Listbox()
        self.appt_list.pack()
        self.appt_list.bind("<Double-Button-1>", self.open_note)
        menu = Menu(root)
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label="New", command=self.new_note)
        menu.add_cascade(label="File", menu=filemenu)
        root.config(menu=menu)
    
    def new_note(self, *args, **kwargs):
        # add date/times
        new_note = Frame(Tk(), padx=10, pady=10)
        new_note.pack()
        Label(new_note, font="15", text="%s %s, %s" % (calendar.month_name[self.month], self.num_selected_day, self.year)).grid()
        time = Frame(new_note)
        Label(time, text="Day").grid(row=0, column=0)
        spin_box = Spinbox(time, width=2)
        spin_box.config(from_=1, to=calendar.monthrange(self.year, self.month)[1])
        [spin_box.invoke('buttonup') for i in range(self.num_selected_day - 1)]
        spin_box.grid(row=0, column=1)
        Label(time, text="Time").grid(row=1, column=0)
        spin_box = Spinbox(time, width=2)
        spin_box.config(from_=1, to=12)
        spin_box.grid(row=1, column=1)
        Label(time, text=":").grid(row=1, column=2)
        spin_box = Spinbox(time, width=2)
        spin_box.config(values=tuple(str(i).zfill(2) for i in range(60)))
        spin_box.grid(row=1, column=3)
        am_pm = StringVar(time)
        am_pm.set("am")
        w = OptionMenu(time, am_pm, "am", "pm")
        w.grid(row=1, column=4)
        time.grid(sticky="w")

        # add message
        f = Frame(new_note)
        f.grid()
        Label(f, text="Message:").pack(anchor="w")
        scrollbar = Scrollbar(f)
        text = Text(f, width=30, height=5, yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)
        scrollbar.pack(side='right', fill='y')
        text.pack(side='left', expand=0, fill='both')

        Button(new_note, text="Save", padx=10, command=self.save_note).grid(pady=10)
            
    def save_note(self, *args, **kwargs):
    	print kwargs

    def select_day(self, arg):
        self.selected_day.config(foreground="BLACK", background="WHITE")
        self.selected_day = arg.widget
        self.selected_day.config(foreground="WHITE", background="BLUE")
        for i, day in enumerate(self.days):
            if self.selected_day == day:
                self.num_selected_day = self.tvs[i].get()
    
    def open_note(self, arg):
    	print self.appt_list.get(arg.widget.curselection()[0])
    
    def add_days(self):
        self.tvs = []
    	for day in self.days:
    	    day.destroy()
        self.days = []
        for i, date in enumerate(self.c.itermonthdates(self.year, self.month)):
            tv = IntVar()
            tv.set(date.day)
            self.tvs.append(tv)
            self.days.append(Label(self.frame, bg="white", width=3, textvariable=tv))
            self.days[-1].grid(row=(i / 7), column=(i % 7))
            if date.month != self.month:
            	self.days[-1].configure(state=DISABLED)
            else:
                if date.day == self.day:
                    self.selected_day = self.days[-1]
                self.days[-1].bind("<Button-1>", self.select_day)
                self.days[-1].bind("<Double-Button-1>", self.new_note)
            	
    def prev_month(self):
    	if self.month <= 1:
    		self.year -= 1
    		self.month = 12
    	else:
    		self.month -= 1
        self.change_month()
    	
    def next_month(self):
    	if self.month >= 12:
    		self.year += 1
    		self.month = 1
    	else:
    		self.month += 1
        self.change_month()

    def change_month(self):
    	self.month_lbl.configure(text=calendar.month_name[self.month] + " " + str(self.year))
        self.add_days()
        
root = Tk()
scheduler = Scheduler(root)
root.mainloop()
    
