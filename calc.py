from tkinter import *
import tkinter.messagebox as msg
root = Tk()

root.title("Calculator")

expression = ""
equation = StringVar()

en = Entry(root,width=35,borderwidth=5,textvariable=equation)
en.grid(padx=10,pady=10,columnspan=4)

def btn_dlt():
    global expression
    en.delete(0,END)

def btn_press(nums):
    global expression
    expression = expression + str(nums)
    equation.set(expression)

def btn_equals():
    try:
        global expression
        t = str(eval(expression))
        equation.set(t)
    except:
        msg.showinfo("Error","It cannot be end like this")



btn1 = Button(root,text="1",padx=40,pady=20,command=lambda:btn_press(1)).grid(row=1,column=0)
btn2 = Button(root,text="2",padx=40,pady=20,command=lambda:btn_press(2)).grid(row=1,column=1)
btn3 = Button(root,text="3",padx=40,pady=20,command=lambda:btn_press(3)).grid(row=1,column=2)
btn4 = Button(root,text="4",padx=40,pady=20,command=lambda:btn_press(4)).grid(row=2,column=0)
btn5 = Button(root,text="5",padx=40,pady=20,command=lambda:btn_press(5)).grid(row=2,column=1)
btn6 = Button(root,text="6",padx=40,pady=20,command=lambda:btn_press(6)).grid(row=2,column=2)
btn7 = Button(root,text="7",padx=40,pady=20,command=lambda:btn_press(7)).grid(row=3,column=0)
btn8 = Button(root,text="8",padx=40,pady=20,command=lambda:btn_press(8)).grid(row=3,column=1)
btn9 = Button(root,text="9",padx=40,pady=20,command=lambda:btn_press(9)).grid(row=3,column=2)
btn0 = Button(root,text="0",padx=40,pady=20,command=lambda:btn_press(0)).grid(row=4,column=0)

btnc = Button(root,text="C",padx=40,pady=20,command=btn_dlt).grid(row=4,column=1)
btne = Button(root,text="=",padx=40,pady=20,command=btn_equals).grid(row=4,column=2)

btnadd = Button(root,text="+",padx=40,pady=20,command=lambda:btn_press("+")).grid(row=1,column=3)
btnsub = Button(root,text="-",padx=40,pady=20,command=lambda:btn_press("-")).grid(row=2,column=3)
btnmulti = Button(root,text="*",padx=40,pady=20,command=lambda:btn_press("*")).grid(row=3,column=3)
btndiv = Button(root,text="/",padx=40,pady=20,command=lambda:btn_press("/")).grid(row=4,column=3)


mainloop()