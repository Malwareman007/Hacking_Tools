#importing mmodules

from tkinter import *
import base64

# Base64 is a group of similar binary-to-text encoding schemes that represent
# #binary data in an ASCII string format by translating it into
# a radix-64 representation.

# initialize window
root = Tk()
root.geometry('540x400')
# size of Frame
root.resizable(0, 0)

# title of the window
root.title("Message Encode and Decode")

# label

Label(root, text='ENCODE DECODE', font='Times 20 bold', justify='center').pack()
# pack shows orientation of label , default is top in pack()
Label(root, text='Open Source', font='arial 20 ', justify='center').pack(side=BOTTOM)

# variables declaration

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


# Encode Method
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# returns decoded text

def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)


def Mode():
    if mode.get() == 'e' or mode.get() == 'E':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'd' or mode.get() == 'D':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


def Exit():
    root.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# Message
Label(root, font='arial 12 ', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(x=300, y=60)

# key
Label(root, font='arial 12 ', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=private_key, bg='ghost white').place(x=300, y=90)

# mode
Label(root, font='arial 12 ', text='MODE (e-encode, d-decode)').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode, bg='ghost white').place(x=300, y=120)

# result
Entry(root, font='arial 14 ', textvariable=Result, bg='ghost white').place(x=300, y=150)

# result button
Button(root, font='arial 10 bold', text='RESULT', padx=2, bg='LimeGreen', command=Mode, bd=3).place(x=60, y=150)

# reset button
Button(root, font='arial 10 bold', text='RESET', width=10, command=Reset, bg='cyan', padx=2, bd=3).place(x=80, y=200)

# exit button
Button(root, font='arial 10 bold', text='EXIT', width=10, command=Exit, bg='OrangeRed', padx=2, pady=2, bd=3).place(
    x=300, y=200)

# Infinite loop
root.mainloop()
