import qrcode, PIL # pillow >PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import  ttk, filedialog,messagebox

#define functions...
def CreateQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)# QR code
        resized_img = img.resize((280,250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Error", "Enter Some Date First")


def SaveQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)  # QR code
        resized_img = img.resize((280, 250))
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Sucess", "QR Code is Saved")
    else:
            messagebox.showwarning("Error","Enter Some Date First")

#GUI code..
root = tk.Tk()
root.title("QR code Generator")
root.geometry("300x380")
root.config(bg="white")
root.resizable(0,0)
#creation of the first frame
frame1 = tk.Frame(root,bd=2,relief=tk.RAISED)
frame1.place(x=10,y=0,width=280,heigh=250)
#creation of the second frame
frame2 = tk.Frame(root,bd=2,relief=tk.SUNKEN)
frame2.place(x=10,y=260,width=280,heigh=100)

cover_img = tk.PhotoImage(file="qrCodeCover.png")
qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW,image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>", SaveQR)
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2,width=25,font=("sitka small",11),justify=tk.CENTER)
text_entry.bind("<Return>",CreateQR)
text_entry.place(x=5,y=5)
text_entry.focus()

btn1 = ttk.Button(frame2,text="Create", width=10, command=CreateQR)
btn1.place(x=25,y=50)

btn2 = ttk.Button(frame2,text="Save", width=10, command=SaveQR)
btn2.place(x=100,y=50)

btn3 = ttk.Button(frame2,text="Exit", width=10, command=root.quit)
btn3.place(x=170,y=50)

root.mainloop()