import pyqrcode
import png
from tkinter import *
from PIL import ImageTk, Image

# address = input("Please enter the url you want the QR code to be generated for: ")
# file_name = input("Please enter the file name under which you want the QR code to be saved: ")
# url = pyqrcode.create(address)
#
# url.png(f"{file_name}.png", scale=8)


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='URL for QR code')
        self.lbl2 = Label(win, text='Name for file')
        self.lbl3 = Label(win, text='Create!')
        self.t1 = Entry(bd=3)
        self.t2 = Entry(bd=3)
        self.btn1 = Button(win, text='Create!')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1 = Button(win, text='Create!', command=self.create_qr_code)
        self.b1.place(x=100, y=150)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)

    def create_qr_code(self):
        self.t2.delete(0, 'end')
        self.t1.delete(0, 'end')
        address = self.t1.get()
        file_name = self.t2.get()
        url = pyqrcode.create(address)
        url.png(f"{file_name}.png", scale=8)

        self.t2.insert(END, url.png(f"{file_name}.png", scale=8))


window = Tk()
mywin = MyWindow(window)
window.title('QR code generator')
window.geometry("500x500+10+10")
window.mainloop()
