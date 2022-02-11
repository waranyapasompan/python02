f =open("myfile2.txt","w")
txt1="Siam Dhurakit \n"
txt1 +="วรัญญา ประสบพันธ์ \n"
txt1 +="Tel. 0923737243"

s = f.write(txt1 )

f.close()

print("เขียนลงไฟล์แล้ว")