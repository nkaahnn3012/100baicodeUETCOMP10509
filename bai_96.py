# 0096 - Viết chương trình con tính tổng các phần tử chẵn
# trong 1 mảng
# Đề bài
# Viết chương trình con tính tổng các phần tử chẵn trong 1 mảng, áp dụng tính trung bình
# cộng các số chẵn trong mảng
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Trung bình cộng các số chẵn trong mảng, làm tròn đến 2 chữ số thập phân
def sum_even_list(number):
    sum = 0
    for i in range(len(number)):
        if number[i] % 2 == 0:
            sum += number[i]
    return sum
n = int(input())
count_even = 0
number = []
for i in range(n):
    j = int(input())
    number.append(j)
for k in range(n):
    if number[k] % 2 == 0:
        count_even += 1
avrg = sum_even_list(number) / count_even
print(f"{avrg:.2f}")