# 0048 - In ra những số chia hết cho 5 và tổng của chúng
# trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. In ra những số chia hết
# cho 5 và tổng của chúng.
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên.
# Dữ liệu ra
# Dòng 1 là những số chia hết cho 5 trong mảng (nếu không có số chia hết cho 5 nào
# trong mảng thì dòng 1 in -), dòng 2 là tổng những số chia hết cho 5
n = int(input())
number = list(map(int, input().split()))
list_5=[]
for i in range(n):
    if number[i] % 5 == 0:
        list_5.append(number[i])
if len != 0:
    for j in range(len(list_5)):
        print(list_5[j], end = " ")
    print()
elif len == 0:
    print("-")
print(sum(list_5))
