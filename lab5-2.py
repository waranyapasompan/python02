def  BMI(w,h):
    bmi = w/pow(h,2)  #หรือ w/h**2
    return bmi

w = int(input("รับค่าส่วนสูง w:"))
h = int(input("รับค่าน้ำหนัก h:"))
ิ
print("ดัชนีมวลกาย(BMI)", BMI(w,h/100))

ิbmi =BMT(w,h/100)
if bmi < 18.5:
    print("น้ำหนักต่ำกว่าเกณ")
elif bmi >= 18.5 and bmi <= 22.9:
    print("สมส่วน")
elif bmi >= 23.0 and bmi <= 24.9:
    print("น้ำหนักเกิน")  
elif bmi >= 25.0 and bmi <= 29.9:
    print("โรคอ้วน")
elif bmi >=30 :
    print("โรคอ้วนอันตราย")