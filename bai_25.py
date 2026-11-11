# 0025 - Tính tổng những số chẵn
# Đề bài
# Viết chương trình nhập vào 1 số nguyên dương n. Tính tổng những số chẵn từ 1 đến n.
# Dữ liệu vào
# Một số nguyên dương n.
# Dữ liệu ra
# tổng các số chẵn từ 1 đến n
n = int(input())
if n % 2 == 0:
    print((n * (n + 2)) // 4)
elif n  % 2 != 0:
    print(((n-1) * (n+1)) // 4)