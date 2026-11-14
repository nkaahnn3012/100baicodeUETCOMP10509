# 0059 - Tìm số nguyên xuất hiện nhiều lần nhất trong mảng
# Đề bài
# Nhập vào 1 mảng số nguyên a có n phần tử. Tìm số nguyên xuất hiện nhiều lần nhất
# trong mảng (nếu có nhiều số cùng xuất hiện nhiều nhất thì lấy số đầu tiên xuất hiện
# nhiều nhất)
# Dữ liệu vào
# Dòng đầu tiên là số nguyên dương n; n dòng tiếp theo là n số nguyên.
# Dữ liệu ra
# Số thứ nhất là giá trị xuất hiện nhiều nhất trong mảng, số thứ 2 là số lần xuất hiện của
# số thứ nhất trong mảng, 2 số cách nhau bởi dấu cách.
n = int(input())
number = []
number_after = []
for i in range(n):
    num = int(input())
    number.append(num)
count = 0
dif = [True] * (len(number))
for i in range(len(number)):
    for j in range (len(number)):
        if dif[i] == False:
            break
        else:
            if number[i] == number[j]:
                if j != i:
                    dif[j] = False
for k in range(len(number)):
    if dif[k] == True:
        number_after.append(number[k])
        count += 1
count_number_of_n = [0] * (len(number_after))
for m in range(len(number_after)):
    for n in range (len(number)):
        if number_after[m] == number[n]:
            count_number_of_n[m] += 1
max = count_number_of_n[0]
for u in range (len(count_number_of_n)):
    if count_number_of_n[u] > max:
        max = count_number_of_n[u]
for v in range(count):
    if max == count_number_of_n[v]:
        print(f"{number_after[v]} {max}")