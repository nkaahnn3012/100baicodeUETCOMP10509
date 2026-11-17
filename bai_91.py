# 0091 - Viết chương trình vẽ hình chữ nhật bằng dấu * sử
# dụng chương trình con
# Đề bài
# Viết chương trình vẽ hình chữ nhật bằng dấu * sử dụng chương trình con
# Dữ liệu vào
# Một dòng gồm 2 số nguyên d và r.
# Dữ liệu ra
# hình chữ nhật rỗng với chiều dài d và chiều rộng r
d, r = map(int,input().split())
if r == 1:
    print("*" * d)
elif r == 2:
    for j in range(2):
        print("*" * d)
elif r >= 2:
    print("*" * d)
    for i in range(r - 2):
        print("*", end = "")
        print(" " * (d - 2), end ="")
        print("*")
    print("*" * d)
