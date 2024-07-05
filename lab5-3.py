def beforeMidterm():
    t = (a + b + c)
    return t


    
a = int(input("ใส่คะแนนเก็บ: "))
if a > 20:
    print("คะแนนเก็บไม่เกิน20")
else:
    b = int(input("ใส่คะแนนจิตพิสัย: "))
    if b > 10:
        print("คะแนนจิตพิสัยไม่เกิน10")
    else:

        c = int(input("ใส่คะแนนกลางภาค: "))
        if c > 20:    
            print("คะแนนกลางภาคไม่เกิน20")
        else:
    
            print("คะแนนรวม %.2f " % beforeMidterm())