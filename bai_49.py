# 0049 - Tìm phần tử lớn nhất đầu tiên trong mảng và vị trí
# của phần tử lớn nhất đó
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Tìm phần tử lớn nhất đầu
# tiên trong mảng và vị trí của phần tử lớn nhất đó
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Gồm 1 dòng chứa số lớn nhất trong mảng và vị trí của số lớn nhất
n = int(input())
number = list(map(int, input().split()))
max = number[0]
index_max = 0
for i in range (n):
    if number[i] > max:
        max = number[i]
        index_max = i
print(f"{max} {index_max}")
