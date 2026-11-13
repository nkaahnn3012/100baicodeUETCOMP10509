# 0054 - Tìm số âm lớn nhất trong mảng
# Đề bài
# Nhập vào 1 mảng số nguyên a có n phần tử. Tìm số âm lớn nhất trong mảng
# Dữ liệu vào
# Gồm 1 dòng chứa các số nguyên, mỗi số cách nhau 1 dấu cách.
# Dữ liệu ra
# Số âm lớn nhất trong mảng (nếu không có số âm nào thì in -)
number = list(map(int, input().split()))
ne_list = []
negative = False
for i in range(len(number)):
    if number[i] < 0:
        negative = True
        ne_list.append(number[i])
if not negative:
    print("-")
elif negative:
    print(max(ne_list))
