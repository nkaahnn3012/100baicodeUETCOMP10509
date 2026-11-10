# 0015 - Kiểm tra a, b, c có là 3 cạnh của một tam giác
# Đề bài
# Viết chương trình kiểm tra xem 3 số a, b, c nhập từ bàn phím có là 3 cạnh của một tam
# giác hay ko? Nếu phải thì tính chu vi và diện tích của tam giác đó, ngược lại thông báo
# 3 số đó ko phải là 3 cạnh của tam giác
# Dữ liệu vào
# Một dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c.
# Dữ liệu ra
# Dòng 1: “Day khong phai la 3 canh cua mot tam giac” hoặc “Day la 3 canh cua mot tam
# giac”, nếu là trường hợp 2 thì thêm dòng 2 là chu vi và diện tích nằm trên cùng một
# dòng, cách nhau bởi dấu cách, chu vi làm tròn đến 2 chữ số thập phân, diện tích làm
# tròn đến 1 chữ số thập phân.
from math import sqrt
a, b, c = map(int, input().split())
cv = a + b + c
p = cv / 2
dt = sqrt(p*(p - a) * (p - b) * (p - c))
if max(a, b, c) >= (cv - max(a, b, c)):
    print("Day khong phai la 3 canh cua mot tam giac")
else:
    print("Day la 3 canh cua mot tam giac")
    print(f"{cv:.2f} {dt:.1f}")