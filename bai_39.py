# 0039 - Kiểm tra số chính phương
# Đề bài
# Viết chương trình kiểm tra 1 số nguyên n có phải là số chính phương hay không? Số
# chính phương là số tự nhiên bằng bình phương của tự nhiên. Vd n=9 là số chính
# phương vì 9=32; n=5 không là số chính phương vì không có số tự nhiên nào bình
# phương lên bằng 5
# Dữ liệu vào
# Một số nguyên dương n
# Dữ liệu ra
# Yes nếu n là số chính phương; No nếu n không phải là số chính phương
from math import sqrt
n = int(input())
c = round(sqrt(n), 0)
if c ** 2 == n:
    print("Yes")
else:
    print("No")