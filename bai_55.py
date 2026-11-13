# 0055 - Tìm số nguyên lớn nhì trong mảng
# Đề bài
# Nhập vào 1 mảng số nguyên a có n phần tử. Tìm số nguyên lớn nhì trong mảng
# Dữ liệu vào
# Gồm 1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách.
# Dữ liệu ra
# Số nguyên lớn nhì trong mảng (nếu không có số nguyên lớn nhì thì in -)
number = list(map(int,input().split()))
max = number[0]
for i in range(len(list(number))):
    if number[i] > max:
        max = number[i]
max_second = number[0]
have_max_second = False
for j in range(len(list(number))):
    if number[j] > max_second and number[j] < max:
        max_second = number[j]
        have_max_second = True
if not have_max_second:
    print("-")
elif have_max_second:
    print(max_second)
