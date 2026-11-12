# 0023 - Tìm những số chia hết cho 3
# Đề bài
# Viết chương trình nhập vào 1 số nguyên dương n. In ra những số chia hết cho 3 trong
# các số từ 1 đến n, nếu không có số nào thì in -.
# Dữ liệu vào
# Một số nguyên dương n
# Dữ liệu ra
# Một dòng các số chia hết cho 3 từ 1 đến n, mỗi số cách nhau 1 dấu cách; nếu không có
# thì in -
n = int(input())
list = []
for i in range (1, n+1):
    if i % 3 == 0:
        list.append(i)
length = len(list)
if length == 0:
    print("-")
else:
    for j in range (length):
        print(list[j], end = " ")
    print()