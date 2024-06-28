#โปรแกรมหาพื้นที่วงกลม
import math
def circle(radius):
    # คำนวณพื้นที่วงกลมโดยใช้สูตร π * r²
    area = math.pi * radius**2
    return area

radius = float(input("ป้อนรัศมีของวงกลม: "))
circle_area = circle(radius)
print("พื้นที่ของวงกลมที่มีรัศมี {radius} คือ {circle_area:.2f}")