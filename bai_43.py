# 0043 - Đếm số chẵn trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Đếm xem trong mảng có
# bao nhiêu số chẵn.
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên
# Dữ liệu ra
# Số lượng số chẵn của dãy số nguyên trên
n = int(input())
number = list(map(int, input().split()))
even = 0
for i in range (n):
    if number[i] % 2 == 0:
        even += 1
print(even)