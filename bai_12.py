# 0012 - Tìm 2 chữ số đầu và 2 chữ số cuối
# Đề bài
# Cho một số nguyên có 3 chữ số. In ra 2 chữ số cuối và 2 chữ số đầu của số vừa nhập
# Dữ liệu vào
# Một số nguyên n có 3 chữ số
# Dữ liệu ra
# Là 2 chữ số đầu và 2 chữ số cuối của n, cách nhau bởi dấu cách (nếu 2 chữ số là 0 thì
# in 00, nếu 2 chữ số mà có 0 phía trước thì vẫn in, vd 05)
# Cach 1:
n = input()
print(n[0], n[1], sep = "", end = " ")
print(n[1], n[2], sep = "")
# Cach 2:
# n = int(input())
# two_first = n // 10
# two_last = n % 100
# print(f"{two_first:02d} {two_last:02d}")

