__author__ = 'Tom'

from Tkinter import *

class Appointment:
    def __init__(self, s):
        # add date/times
        new_note = Frame(Tk(), padx=10, pady=10)
        new_note.pack()
        Label(new_note, font="15", text=s.get_full_lbl()).grid()
        time = Frame(new_note)
        Label(time, text="Day").grid(row=0, column=0)
        spin_box = Spinbox(time, width=2)
        spin_box.config(from_=1, to=s.days_in_month())
        [spin_box.invoke('buttonup') for i in range(s.date["day"] - 1)]
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
        scroll_bar = Scrollbar(f)
        text = Text(f, width=30, height=5, yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=text.yview)
        scroll_bar.pack(side='right', fill='y')
        text.pack(side='left', expand=0, fill='both')

        Button(new_note, text="Save", padx=10, command=self.save_note).grid(pady=10)

    def save_note(self, *args, **kwargs):
    	print kwargs