#  0056 - Tìm số nguyên nhỏ thứ 3 trong mảng
# Đề bài
# Nhập vào 1 mảng số nguyên a. Tìm số nguyên nhỏ thứ 3 trong mảng
# Dữ liệu vào
# Gồm nhiều dòng chứa các số nguyên, mỗi số 1 dòng.
# Dữ liệu ra
# Số nguyên nhỏ thứ 3 trong mảng (nếu không có số nguyên nhỏ thứ 3 thì in -)
import sys
number = list(map(int,sys.stdin.read().split()))
min = number[0]
for i in range(len(number)):
    if number[i] < min:
        min = number[i]
min_second = number[0]
min_third = number[0]
have_min_third = False
for j in range(len(number)):
    if number[j] < min_second and number[j] > min:
        min_second = number[j]
for k in range(len(number)):
    if number[k] < min_third and number[k] > min_second:
        min_third = number[k]
        have_min_third = True
if not have_min_third:
    print("-")
elif have_min_third:
    print(min_third)