# 0044 - Tính tổng các phần tử ở vị trí chẵn trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Tính tổng các phần tử ở vị
# trí chẵn.
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Tổng các phần tử ở vị trí chẵn của dãy số nguyên trên
n = int(input())
number = list(map(int, input().split()))
sum_even_index = 0
for i in range (n):
    if i % 2 == 0:
        sum_even_index += number[i]
print(sum_even_index)