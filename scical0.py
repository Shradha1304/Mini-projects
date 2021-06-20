import tkinter
from tkinter import *
from tkinter import messagebox
import math

root = Tk()
root.geometry("650x400+300+300")

switch = None


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def event(*arg):
    if disp.get() == '0':
        disp.delete(0, END)


def plus_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def sub_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def multi_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def divide_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*arg):
    disp.delete(0, END)
    disp.insert(0, '0')


def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def arcsin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.asin(math.radians(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def arccos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.acos(math.radians(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def arctan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.atan(math.radians(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def xy_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')


def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def log_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def sroot_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, float(math.pi))


def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, float(math.pi))


def b1_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')


def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos - 1])


def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "deg"
    else:
        switch = None
        conv_btn['text'] = "rad"


def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, float(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")


def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, "%")


def btneq_clicked():
    try:
        ans = str(disp.get())
        disp.delete(0, END)
        disp.insert(0, str(ans))

    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check you values and operater")

# --------------------------
data = StringVar()

disp = Entry(root, font="verdana 20", fg="black", bg="gray", bd=0, justify=RIGHT, insertbackground="#abbab1",
             cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("1", event)
disp.bind("2", event)
disp.bind("3", event)
disp.bind("4", event)
disp.bind("5", event)
disp.bind("6", event)
disp.bind("7", event)
disp.bind("8", event)
disp.bind("9", event)
disp.bind("0", event)
disp.bind(",", event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=True, fill=BOTH)

btnrow1 = Frame(root, bg="black")
btnrow1.pack(expand=True, fill=BOTH)

pi_btn = Button(btnrow1, text="pi", font="segoe 18", relief=GROOVE, bd=0, command=pi_clicked, fg="white", bg="#333333")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text="x!", font="segoe 18", relief=GROOVE, bd=0, command=fact_clicked, fg="white",
                  bg="#333333")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="segoe 18", relief=GROOVE, bd=0, command=sin_clicked, fg="white",
                 bg="#333333")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="segoe 18", relief=GROOVE, bd=0, command=cos_clicked, fg="white",
                 bg="#333333")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="segoe 18", relief=GROOVE, bd=0, command=tan_clicked, fg="white",
                 bg="#333333")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1_btn = Button(btnrow1, text="1", font="segoe 18", relief=GROOVE, bd=0, command=btn1_clicked, fg="white",
                  bg="#333333")
btn1_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2_btn = Button(btnrow1, text="2", font="segoe 18", relief=GROOVE, bd=0, command=btn2_clicked, fg="white",
                  bg="#333333")
btn2_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3_btn = Button(btnrow1, text="3", font="segoe 18", relief=GROOVE, bd=0, command=btn3_clicked, fg="white",
                  bg="#333333")
btn3_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

plus_btn = Button(btnrow1, text="+", font="segoe 18", relief=GROOVE, bd=0, command=plus_clicked, fg="white",
                  bg="#333333")
plus_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

# -------------------------------------------------------------------
btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill=BOTH)

e_btn = Button(btnrow2, text="e", font="segoe 18", relief=GROOVE, bd=0, command=e_clicked, fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sroot_btn = Button(btnrow2, text="x^(1/2)", font="segoe 18", relief=GROOVE, bd=0, command=sroot_clicked, fg="white",
                   bg="#333333")
sroot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

arcsin_btn = Button(btnrow2, text="sin-1", font="segoe 18", relief=GROOVE, bd=0, command=arcsin_clicked, fg="white",
                    bg="#333333")
arcsin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

arccos_btn = Button(btnrow2, text="cos-1", font="segoe 18", relief=GROOVE, bd=0, command=arccos_clicked, fg="white",
                    bg="#333333")
arccos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

arctan_btn = Button(btnrow2, text="tan-1", font="segoe 18", relief=GROOVE, bd=0, command=arctan_clicked, fg="white",
                    bg="#333333")
arctan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4_btn = Button(btnrow2, text="4", font="segoe 18", relief=GROOVE, bd=0, command=btn4_clicked, fg="white",
                  bg="#333333")
btn4_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5_btn = Button(btnrow2, text="5", font="segoe 18", relief=GROOVE, bd=0, command=btn5_clicked, fg="white",
                  bg="#333333")
btn5_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6_btn = Button(btnrow2, text="6", font="segoe 18", relief=GROOVE, bd=0, command=btn6_clicked, fg="white",
                  bg="#333333")
btn6_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sub_btn = Button(btnrow2, text="-", font="segoe 18", relief=GROOVE, bd=0, command=sub_clicked, fg="white", bg="#333333")
sub_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
# ------------------------------------------------------------------------
btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill=BOTH)

conv_btn = Button(btnrow3, text="rad", font="segoe 18", relief=GROOVE, bd=0, command=conv_clicked, fg="white",
                  bg="#333333")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="round", font="segoe 18", relief=GROOVE, bd=0, command=round_clicked, fg="white",
                   bg="#333333")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

log_btn = Button(btnrow3, text="log", font="segoe 18", relief=GROOVE, bd=0, command=log_clicked, fg="white",
                 bg="#333333")
log_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="segoe 18", relief=GROOVE, bd=0, command=ln_clicked, fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

xy_btn = Button(btnrow3, text="x^y", font="segoe 18", relief=GROOVE, bd=0, command=xy_clicked, fg="white", bg="#333333")
xy_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7_btn = Button(btnrow3, text="7", font="segoe 18", relief=GROOVE, bd=0, command=btn7_clicked, fg="white",
                  bg="#333333")
btn7_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8_btn = Button(btnrow3, text="8", font="segoe 18", relief=GROOVE, bd=0, command=btn8_clicked, fg="white",
                  bg="#333333")
btn8_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9_btn = Button(btnrow3, text="9", font="segoe 18", relief=GROOVE, bd=0, command=btn9_clicked, fg="white",
                  bg="#333333")
btn9_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

multi_btn = Button(btnrow3, text="*", font="segoe 18", relief=GROOVE, bd=0, command=multi_clicked, fg="white",
                   bg="#333333")
multi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

# -----------------------------------------------------------------
btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="segoe 18", relief=GROOVE, bd=0, command=mod_clicked, fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

b1_btn = Button(btnrow4, text="(", font="segoe 18", relief=GROOVE, bd=0, command=b1_clicked, fg="white", bg="#333333")
b1_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=")", font="segoe 18", relief=GROOVE, bd=0, command=br_clicked, fg="white", bg="#333333")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=".", font="segoe 18", relief=GROOVE, bd=0, command=dot_clicked, fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc_btn = Button(btnrow4, text="C", font="segoe 18", relief=GROOVE, bd=0, command=btnc_clicked, fg="white",
                  bg="#333333")
btnc_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="del", font="segoe 18", relief=GROOVE, bd=0, command=del_clicked, fg="white",
                 bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq_btn = Button(btnrow4, text="=", font="segoe 18", relief=GROOVE, bd=0, command=btneq_clicked, fg="white",
                   bg="#333333")
btneq_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0_btn = Button(btnrow4, text="0", font="segoe 18", relief=GROOVE, bd=0, command=btn0_clicked, fg="white",
                  bg="#333333")
btn0_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

divide_btn = Button(btnrow4, text="/", font="segoe 18", relief=GROOVE, bd=0, command=divide_clicked, fg="white",
                    bg="#333333")
divide_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

root.mainloop()

