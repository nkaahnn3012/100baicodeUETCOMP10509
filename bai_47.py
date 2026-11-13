# 0047 - Đếm và in dãy số dương, số âm trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Đếm xem trong dãy số có
# bao nhiêu số dương, bao nhiêu số âm? In ra dãy các số dương, dãy các số âm.
# Dữ liệu vào
# Dòng 1 là số nguyên dương n, dòng 2 là n số nguyên
# Dữ liệu ra
# Dòng 1 gồm 2 số: số số dương và số số âm trong dãy (nếu không có số dương nào thì
# in số 0; nếu không có số âm nào thì in số 0); dòng 2 là dãy các số dương (nếu không
# có số nguyên dương nào trong mảng thì in -), dòng 3 là dãy các số âm (nếu không có
# số nguyên âm nào thì in -); các số cách nhau bởi dâu cách.
n = int(input())
number = list(map(int,input().split()))
list_po = []
list_ne = []
number_po = 0
number_ne = 0
for i in range (n):
    if number[i] > 0:
        list_po.append(number[i])
        number_po += 1
    elif number[i] < 0:
        list_ne.append(number[i])
        number_ne += 1
print(f"{number_po} {number_ne}")
if number_po == 0:
    print("_")
else:
    for i in range(len(list_po)):
        print(list_po[i], end = " ")
    print()
if number_ne == 0:
    print("_")
else:
    for j in range(len(list_ne)):
        print(list_ne[j], end = " ")
    print()