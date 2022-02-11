try:
    num = int(input("ป้อนค่าตัวเลข"))
    circle = 3.14*num**2 #3.14*pow(num,2)
    
except:
    print("error ครับผม")
    
else:
    print("คำตอบ",circle)