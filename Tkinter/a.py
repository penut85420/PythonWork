from tkinter import Frame, Tk, StringVar, Entry, IntVar, Button

class App(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.entry = Entry()
		self.entry.pack()
		self.number = Entry()
		self.number.pack()
		self.check = Button(self, {'text': 'hello', 'command': self.print_check})
		self.check.pack()

		self.contents = StringVar()
		self.contents.set('This is a StringVar')
		self.entry['textvariable'] = self.contents
		self.entry.bind('<Key-Return>', self.print_contents)

		self.id = IntVar()
		self.id.set('0')
		self.number['textvariable'] = self.id
		self.number.bind('<Key-Return>', self.print_id)

	def print_contents(self, e):
		print('Hi, contents of entry is now', self.contents.get())

	def print_id(self, e):
		print('Hello,', self.id.get())

	def print_check(self):
		print(self.id, self.contents)

def main():
	tk = Tk()
	app = App(tk)
	app.master.title('Hello, Tkinter')
	# app.master.maxsize(400, 300)
	# app.master.minsize(400, 300)
	app.mainloop()
	print('App Exit')
main()