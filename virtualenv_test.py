# from tkinter import *
# class Application (Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#     def createWidgets(self):
#         self.helloLable=Label(self,text='Hello,world')
#         self.helloLable.pack()
#         self.quitButton=Button(self,text='Quit',command=self.quit)
#         self.quitButton.pack()
#
# app = Application()
# app.master.title('ello,world?')
# app.mainloop()

from tkinter import *
import tkinter.messagebox as messagebox
class Applicatio(Frame):
    def __init__(self,maste=None):
        Frame.__init__(self,maste)
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','hello,%s' % name)
app = Applicatio()
app.master.title('hello,title')
app.mainloop()