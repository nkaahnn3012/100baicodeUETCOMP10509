# 0093 - Sử dụng hàm tìm số nhỏ nhất trong 2 số để tìm số
# nhỏ nhất trong 3 số
# Đề bài
# Viết chương trình cho biết giá trị nhỏ nhất trong 3 số nhập từ bàn phím, trong đó có sử
# dụng hàm tìm số nhỏ nhất trong 2 số.
# Dữ liệu vào
# Gồm 1 dòng có 3 số cách nhau bởi dấu cách theo thứ tự là a, b và c.
# Dữ liệu ra
# Số nhỏ nhất trong 3 số a, b, c.

def min(a, b):
    if a <= b:
        return a
    elif a > b:
        return b
a, b, c = map(int,input().split())
min = min(min(a,b), c)
print(min)