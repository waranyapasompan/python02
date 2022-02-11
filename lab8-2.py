def cal():
    r = int(tb1.get())
    circle = (3.14)*r*r
    result.set(circle)
    messagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์ %.2f " % circle)
    
from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย วรัญญา เจนเนอร์")

result = StringVar()

lb = Label(window , text="ยินดีต้อนรับเข้าสู่ Python", font=("Tahoma",24))
lb.place(x=50, y=10)

lb2 = Label(window , text="รับค่ารัศมี", font=("Tahoma",18))
lb2.place(x=50, y=100)

tb1 = Entry(window)
tb1.place(x=180, y=110 , width=200, height=30)

lb3 = Label(window , text="ผลลัพธ์", font=("Tahoma",24))
lb3.place(x=50, y=150)

tb2 = Entry(window,textvariable = result)
tb2.place(x=180, y=170, width=200, height=30)

btn = Button(window, text="คำนวณ", font=("Tahoma",20), command=cal)
btn.place(x=400, y=100)

window.mainloop()
          
