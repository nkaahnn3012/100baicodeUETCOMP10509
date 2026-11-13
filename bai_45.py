# 0045 - Tính tổng các phần tử có giá trị chẵn trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Tính tổng các phần tử có
# giá trị chẵn (nếu không có số chẵn nào trong mảng thì dòng 1 in -).
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Tổng các số chẵn của dãy số nguyên trên
n = int(input())
number = list(map(int, input().split()))
sum_even = 0
number_even = 0
for i in range (n):
    if number[i] % 2 == 0:
        sum_even += number[i]
        number_even += 1
if number_even == 0:
    print("-")
else:
    print(sum_even)