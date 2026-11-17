# 0097 - Đếm xem trong mảng có bao nhiêu số nguyên tố có
# sử dụng hàm
# Đề bài
# Viết chương trình con kiểm tra 1 số nguyên n có phải là số nguyên tố hay không? Áp
# dụng đếm xem trong mảng có bao nhiêu số nguyên tố
# Dữ liệu vào
# Gồm 1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách
# Dữ liệu ra
# số lượng số nguyên tố trong mảng (nếu không có số nguyên tố nào thì in -)
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
for j in range(len(number)):
    if is_prime(number[j]):
        count_prime += 1
if count_prime == 0:
    print("-")
else:
    print(count_prime)