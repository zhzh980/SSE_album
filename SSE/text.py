# from tkinter import *
# class Application(Frame):
#     def __init__(self,master = None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLable = Label(self,text ="hello world")
#         self.helloLable.pack()
#         self.quitButton = Button(self,text = "退出",command = self.quit)
#         self.quitButton.pack()
#
# app = Application()
# app.master.title = "hello world"
# app.mainloop()


from tkinter import *
from PIL import Image,ImageFilter
import tkinter.messagebox as messagebox

im1 = Image.open("button01_a.jpg")
w,h = im1.size
im2 = im1.filter(ImageFilter.BLUR)
im1.thumbnail((w/2,h/2))
im1.save("thumbnail.jpg","jpeg")
im2.save("Blur.jpg","jpeg")


class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self,text = "Hello",command = self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or "world"
        messagebox.showinfo("Message","Hello,{}".format(name))

app = Application()
app.master.title('hello world')
app.mainloop()
