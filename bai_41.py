# 0041 - Tính tổng các phần tử trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Tính tổng các phần tử của
# mảng đó.
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Tổng của dãy số nguyên trên
n = int(input())
number = list(map(int,input().split()))
sum = 0
for i in range(n):
    sum += number[i]
print(sum)