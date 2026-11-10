# 0006 - Tính chu vi và diện tích của một tam giác
# Đề bài
# Viết chương trình tính chu vi (cv) và diện tích (s) một tam giác có 3 cạnh a, b, c là các
# số nguyên theo công thức cv=a+b+c, s=sqrt(p*(p-a)*(p-b)*(p-c)) với p=cv/2 (3 số a, b, c
# bảo đảm là 3 cạnh của 1 tam giác).
# Dữ liệu vào
# Gồm 1 dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c.
# Dữ liệu ra
# Là chu vi và diện tích nằm trên cùng một dòng, cách nhau bởi dấu cách, chu vi làm tròn
# đến 1 chữ số thập phân, diện tích làm tròn đến 3 chữ số thập phân.
from math import sqrt
a, b, c = map(int, input().split())
cv = a + b + c
p = cv / 2
dt = sqrt(p*(p - a)*(p - b)*(p - c))
print(f"{cv:.1f} {dt:.3f}")