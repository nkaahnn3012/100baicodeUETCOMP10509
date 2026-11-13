# 0050 - Sắp xếp mảng theo thứ tự tăng dần
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Sắp xếp mảng theo thứ tự
# tăng dần.
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Gồm 1 dòng chứa các số trong mảng theo thứ tự tăng dần
n = int(input())
number = list(map(int, input().split()))

for i in range(n):
    swapped = False
    for j in range(n - 1):
        if number[j] > number [j + 1]:
            number[j], number[j+1] = number[j + 1], number [j]
            swapped = True
    if not swapped:
        break
print(*number)

