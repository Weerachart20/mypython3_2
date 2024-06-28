#โปรแกรมหาดัชนีมวลกาย
weight = float( input('กรุณากรอกน้ำหนัก (กิโลกรัม) : ') )
height = float( input('กรุณากรอกความสูง (เซนติเมตร) : ') )

def bmi (kg,cm):
    bmi = kg/(cm/100)**2
    return bmi
    

def compare (bmi):
    if bmi < 18.50:
        print("นํ้าหนักน้อย")
    elif bmi >= 18.5 and bmi <= 22.90:
        print("ปกติสุขภาพดี")
    elif bmi >= 23 and bmi <= 24.90:
        print("ท้วม/โรคอ้วนระดับ 1")
    elif bmi >= 25 and bmi <= 29.90:
        print("อ้วน/โรคอ้วนระดับ 2")
    elif bmi >= (30):
        print("อ้วนมาก/โรคอ้วนระดับ 3")
        
print("BMI = %.2f" % bmi(weight,height))
compare(bmi(weight,height))
