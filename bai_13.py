# 0013 - Tìm số lớn nhất trong 3 số
# Đề bài
# Viết chương trình nhập vào 3 số nguyên a, b, c; in ra số lớn nhất, nếu 3 số bằng nhau
# thì in dấu "="
# Dữ liệu vào
# Một dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c
# Dữ liệu ra
# Số lớn nhất trong 3 số a, b, c hoặc dấu =
number = list(map(int, input().split()))
if number[0] == number [1] and number [1] == number [2]:
    print("=")
else:
    max = number[0]
    for n in number:
        if n > max:
            max = n
    print(max)