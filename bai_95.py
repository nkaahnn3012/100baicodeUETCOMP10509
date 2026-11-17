# 0095 - Viết chương trình con tính tổng các phần tử trong 1
# mảng
# Đề bài
# Viết chương trình con tính tổng các phần tử trong 1 mảng, áp dụng tính trung bình cộng
# các số trong mảng
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Trung bình cộng các số trong mảng làm tròn đến 1 chữ số thập phân
def sum_list(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum
n = int(input())
number = []
for j in range(n):
    j = int(input())
    number.append(j)
avrg = sum_list(number) / n
print(f"{avrg:.1f}")

