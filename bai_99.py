# 0099 - Tính trung bình cộng các số chính phương trong
# mảng có sử dụng hàm
# Đề bài
# Viết một chương trình con kiểm tra 1 số nguyên n có phải là số chính phương hay
# không? Áp dụng tính trung bình cộng các số chínhphương trong mảng
# Dữ liệu vào
# Gồm1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách.
# Dữ liệu ra
# Trung bình cộng các số chính phương trong mảng, làm tròn đến 1 chữ số thập phân
# (nếu không có số chính phương nào thì in -)
from math import sqrt
def is_square(n):
    if n < 0:
        return False
    else:
        can_n = int(sqrt(n))
        if n - can_n ** 2 == 0:
            return True
        else:
            return False
number = list(map(int, input().split()))
sum_square = 0
count_square = 0
for i in range (len(number)):
    if is_square(number[i]):
        sum_square += number[i]
        count_square += 1
if count_square == 0:
    print("-")
else:
    avrg = sum_square / count_square
    print(f"{avrg:.1f}")