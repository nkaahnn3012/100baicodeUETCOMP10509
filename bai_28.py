# 0028 - Đếm số ước của số nguyên n
# Đề bài
# Viết chương trình nhập vào 1 số nguyên dương n. Đếm xem n có bao nhiêu ước
# Dữ liệu vào
# Một số nguyên dương n
# Dữ liệu ra
# Số ước của n
from math import sqrt
n = int(input())
s = round(sqrt(n)) // 1
uoc = 0
for i in range(1, s + 1):
    if n % i == 0:
        uoc += 1
print(uoc * 2)