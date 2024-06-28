#ชนิดข้อมูล Dictionary
x = {"name": "Weerachart",
"age":17,
"wt":53,
"h":177
    
}
print(x)
print("สวัสดีครับคุณ %s" %x["name"])
print("พ.ศ.เกิด %d อายุ %d" %(2567-x["age"], x["age"]))
print("น้ำหนัก %d ส่วนสูง  %d" %(x["wt"],x["h"]))
print("วันเกิด %d ")