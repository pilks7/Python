#boilerplate
import tkinter as tk
import subprocess

class App(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.pack()
		self.master.title("Hello World")
		self.master.resizable(False, False)
		self.master.tk_setPalette(background='#ececec')

#BUTTONS
#		tk.Button(self, text='OK', default='active', command=self.click_ok).pack(side='right')		
#		tk.Button(self, text='Cancel', command=self.click_cancel).pack(side='right')
#!!!BROKEN!!!(wrong indent?)sets window location on screen :
#		y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
#		self.master.geometry("+{}+{}".format(x, y))
#		self.master.config(menu= tk.Menu(self.master))

		tk.Label(self, text="This is your first GUI. (highfive)").pack()

		button_frame = tk.Frame(self)
		button_frame.pack(padx=15, pady=(0, 15), anchor='e')

		tk.Button(button_frame, text='OK', default='active', command=self.click_ok).pack(side='right')
		tk.Button(button_frame, text='Cancel', command=self.click_cancel).pack(side='right')

		self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
		self.master.bind('<Return>', self.click_ok)
		self.master.bind('<Escape>', self.click_cancel)

	def click_ok(self):
		print("the user clicked OK")

	def click_cancel(self):
		print("the user clicked cancel")
		self.master.destroy()


if __name__=='__main__':
	root = tk.Tk()
	app = App(root)
	app.mainloop()
	subprocess.call()



