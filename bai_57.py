# 0057 - Đếm số lượng số nguyên khác nhau
# Đề bài
# Nhập vào 1 mảng số nguyên a. Đếm xem trong mảng có bao nhiêu số nguyên khác
# nhau
# Dữ liệu vào
# Gồm nhiều dòng chứa các số nguyên, mỗi số 1 dòng.
# Dữ liệu ra
# Số lượng số nguyên khác nhau trong mảng
import sys
number = list(map(int, sys.stdin.read().split()))
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
        count += 1
print(count)