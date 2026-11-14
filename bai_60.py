# 0060 - Tính trung bình cộng các số chính phương trong
# mảng
# Đề bài
# Nhập vào 1 mảng số nguyên a có n phần tử. Tính trung bình cộng các số chính
# phương trong mảng
# Dữ liệu vào
# Gồm 1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách.
# Dữ liệu ra
# Trung bình cộng các số chính phương trong mảng, làm tròn đến 1 chữ số thập phân
# (nếu không có số chính phương nào thì in -)
from math import sqrt
def is_square(n):
    if n < 0:
        return False
    else:
        c = round(sqrt(n), 0)
        if  c ** 2 == n:
            return True
        else:
            return False
number = list(map(int, input().split()))
count_square = 0
sum = 0
for i in range(len(number)):
    if is_square(number[i]):
        sum += number[i]
        count_square += 1
square_average = sum / count_square
if count_square == 0:
    print("-")
else:
    print(f"{square_average:.1f}")