from tkinter import *
import qrcode
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import os

window = Tk()
window.title("QRcode Result")
window.geometry("400x350")
window.resizable(False, False)
frame = Frame(window)
frame.pack(fill=BOTH, expand=True, padx=20, pady=20)


print("\n\nWELCOME TO QRCODEKU.id\n=======================")
print("1. QRcode Generator\n2. QRcode Scanner\n")
menu = input("Select a menu (1,2): ")

if menu == "1":
    someText = input("\nInput some text or url, i'll convert it to qrcode : ")
    fileName = input("Input a text to name your file : ")
    extension = input("Choose your extension (jpg,jpeg,png): ")

    img = qrcode.make(someText)
    extension = extension.lower()
    saveFile = f"{fileName}.{extension}"
    dir_path = rf"{os.getcwd()}\qr_storage"
    if not os.path.exists(dir_path):
        os.mkdir(os.path.join(os.getcwd(), "qr_storage"))

    img.save(rf"{dir_path}\{saveFile}")
    photo = ImageTk.PhotoImage(
        Image.open(rf"{os.getcwd()}\qr_storage\{saveFile}").resize((150, 150))
    )
    Label(
        frame,
        text="QRcode Created Successfully!",
        font=("Helvetica", 16, "bold"),
        fg="black",
        padx=10,
        pady=10,
    ).pack()
    Label(
        frame,
        font=("Helvetica", 16, "bold"),
        image=photo,
        compound="top",
        pady=25,
    ).pack()
    Label(
        frame,
        text=rf"QRcode saved in {dir_path}",
        font=("Helvetica", 12),
        pady=25,
        wraplength=350,
    ).pack()

elif menu == "2":
    print("Note : please put your qrcode image file in qr_storage directory first!!")
    file_name = input("\nEnter your qrcode filename : ")
    extension = input("Input your qrcode file extension (jpg,jpeg,png): ")
    open_file = f"{file_name}.{extension}"
    data = decode(Image.open(rf"{os.getcwd()}\qr_storage\{open_file}"))
    print("\n")
    photo = ImageTk.PhotoImage(
        Image.open(rf"{os.getcwd()}\qr_storage\{open_file}").resize((150, 150))
    )

    Label(
        frame,
        text="Scanning Success..",
        font=("Helvetica", 20, "bold"),
        fg="#14f52a",
        bg="black",
        padx=10,
        pady=10,
    ).pack()
    Label(
        frame,
        text=f"\"{data[0].data.decode('ascii')}\"",
        font=("Helvetica", 16, "bold"),
        image=photo,
        compound="top",
        pady=25,
    ).pack()

window.mainloop()
