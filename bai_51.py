# 0051 - In ra các số nguyên tố trong mảng và tổng của chúng
# Đề bài
# Nhập vào 1 mảng số nguyên a. In ra các số nguyên tố trong mảng và tổng của chúng
# Dữ liệu vào
# Gồm 1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách.
# Dữ liệu ra
# Dòng 1 chứa các số nguyên tố trong mảng (nếu không có số nguyên tố nào trong mảng
# thì dòng 1 in -), dòng 2 là tổng các số nguyên tố trong mảng
from math import sqrt
number = list(map(int, input().split()))
sum = 0
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
                sum += x
                print(x, end = " ")
print()
print(sum)