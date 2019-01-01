# Ref: https://www.python-course.eu/tkinter_entry_widgets.php
from tkinter import *

class App(Frame):
	def __init__(self, master=None, cnf={}, **kw):
		super().__init__(master=master, cnf=cnf, **kw)
		self.l1 = Label(self, text='Label 1')
		self.l2 = Label(self, text='Lebel 2')
		self.l1.grid(row=3, column=3)
		self.l2.grid(row=5, column=0)
		self.pack()

def main():
	app = App(Tk())
	app.mainloop()
main()