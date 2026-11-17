# 0098 - Tính trung bình cộng các số nguyên tố trong mảng
# có sử dụng hàm
# Đề bài
# Viết chương trình con kiểm tra 1 số nguyên n có phải là số nguyên tố hay không? Áp
# dụng tính trung bình cộng các số nguyên tố trong mảng
# Dữ liệu vào
# Gồm 1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách.
# Dữ liệu ra
# Trung bình cộng các số nguyên tố trong mảng, làm tròn đến 2 chữ số thập phân (nếu
# không có số nguyên tố nào thì in -)
from math import sqrt
def is_prime(n):
    if n <= 0:
        return False
    else:
        if n == 2 or n == 3:
            return True
        uoc = int(sqrt(n)) + 1
        for i in range(2, uoc + 1):
            if n % i == 0:
                return False
        return True
number = list(map(int, input().split()))
count_prime = 0
sum_prime = 0
for j in range(len(number)):
    if is_prime(number[j]):
        count_prime += 1
        sum_prime += number[j]
if count_prime == 0:
    print("-")
else:
    avrg = sum_prime / count_prime
    print(f"{avrg:.2f}")