# 0029 - Kiểm tra số n có nguyên tố
# Đề bài
# Viết chương trình nhập vào 1 số nguyên dương n. Cho biết n có phải là số nguyên tố
# hay không? Số nguyên tố là số chỉ chia hết cho 1 và chính nó (chỉ có 2 ước)
# Vd: n=7 là số nguyên tố vì 7 chỉ chia hết cho 1 và 7
# n=8 Không là số nguyên tố vì 8 chia hết cho 1 và 8 nhưng còn chia hết cho 2 và 4
# Dữ liệu vào
# Số nguyên dương n
# Dữ liệu ra
# Yes nếu n là số nguyên tố; No nếu n không phải là số nguyên tố
from math import sqrt
n = int(input())
s = round(sqrt(n)) // 1
uoc = 0
for i in range(1, s + 1):
    if n % i == 0:
        uoc += 1
uoc *= 2
if uoc == 2:
    print("Yes")
else:
    print("No")