# 0100 - Viết 2 chương trình con tìm Max, Min và vị trí của
# Max, Min trong mảng
# Đề bài
# Viết 2 chương trình con tìm Max, Min và vị trí của Max, Min trong mảng. Áp dụng: Nhập
# vào 1 mảng có 1 phần tử là các số nguyên, tìm số nguyên lớn nhất, nhỏ nhất và vị trí
# của các số đó trong mảng
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên
# Dữ liệu ra
# Gồm 2 dòng: dòng 1 chứa số lớn nhất trong mảng và các vị trí của số lớn nhất; dòng 2
# chứa số nhỏ nhất trong mảng và các vị trí của số nhỏ nhất
def max(number):
    max = number[0]
    index_max = 0
    for i in range (len(number)):
        if number[i] > max:
            max = number[i]
            index_max = i
    return max, index_max

def min(number):
    min = number[0]
    index_min = 0
    for j in range(len(number)):
        if number[j] < min:
            min = number[j]
            index_min = j
    return min, index_min
n = int(input())
number = []
for k in range(n):
    a = int(input())
    number.append(a)
max, index_max = max(number)
min, index_min = min(number)
print(max, index_max)
print(min, index_min)