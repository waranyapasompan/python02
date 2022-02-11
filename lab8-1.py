import tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โดย วรัญญา เจนเนอร์")
messagebox.showninfo("hello","สวัสดีครับ")
messagebox.showwarning("เตือน","ตั้งใจเรียนด้วย")
messagebox.showerror("ผิดพลาด","โปรแกรม error")
messagebox.askquestion("confirmm","คุณต้องการลบ?")
messagebox.askokcancel("confirmm","คุณต้องการลบ?")
messagebox.askyesno("confirmm","คุณต้องการลบ?")
messagebox.askretrycancel("confirmm","คุณต้องการลบ?")


main.mainloop()
