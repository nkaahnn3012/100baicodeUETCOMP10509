# 0086 - Tính chu vi và diện tích của tam giác có sử dụng
# hàm
# Đề bài
# Viết chương trình tính chu vi và diện tích của tam giác, với đoạn nhập 3 cạnh là 1 thủ
# tục, đoạn tính chu vi là 1 hàm, đoạn tính diện tích là 1 hàm.
# Dữ liệu vào
# Gồm 1 dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c (là 3 cạnh
# của 1 tam giác)
# Dữ liệu ra
# Là chu vi và diện tích nằm trên cùng một dòng, cách nhau bởi dấu cách, chu vi làm tròn
# đến 1 chữ số thập phân, diện tích làm tròn đến 3 chữ số thập phân.
from math import sqrt
def compute_perimeter(a, b, c):
    return a + b + c
def compute_area(a, b, c):
    p = (a+ b+ c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))
a, b, c = map(int, input().split())
if max (a, b, c) >= (a + b + c) - max(a, b, c):
    raise ValueError
else:
    perimeter = compute_perimeter(a, b, c)
    area = compute_area(a, b, c)
    print(f"{perimeter:.1f} {area:.3f}")
