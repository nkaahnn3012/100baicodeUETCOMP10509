# 0042 - Đếm số dương trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Đếm xem trong mảng có
# bao nhiêu số dương
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Số lượng số dương của dãy số nguyên trên
n = int(input())
number = list(map(int,input().split()))
positive = 0
for i in range (n):
    if number[i] > 0:
        positive += 1
print(positive)