# 0053 - Tìm số nguyên tố lớn nhất trong mảng
# Đề bài
# Nhập vào 1 mảng số nguyên a. Tìm số nguyên tố lớn nhất trong mảng
# Dữ liệu vào
# Gồm 1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách.
# Dữ liệu ra
# Số nguyên tố lớn nhất trong mảng (nếu không có số nguyên tố nào thì in -)
from math import sqrt
number = list(map(int, input().split()))
sum = 0
count = 0
list = []
n  = max(number)
prime = False
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(sqrt(n)) + 1):
    if is_prime[i]:
        prime = True
        for j in range(i ** 2, n + 1, i):
            is_prime[j] = False
if not prime:
    print("-")
else:
    for x in number:
        if x > 0:
            if is_prime[x]:
                list.append(x)
print(max(list))