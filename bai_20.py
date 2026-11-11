# 0020 - Đổi tiền
# Đề bài
# Nhập một số tiền N (N<=1.000.000) đồng (N là số chia hêt cho 1.000), đổi ra xem được
# bao nhiêu tờ 5.000 đồng, bao nhiêu tờ 2.000 đồng, bao nhiêu tờ 1.000 đồng sao cho
# tổng số tờ là ít nhất. Ví dụ N= 43.000 đ = 8 tờ 5.000 đ + 1 tờ 2.000 đ + 1 tờ 1.000 đ.
# Dữ liệu vào
# Một số nguyên n là số tiền cần đổi
# Dữ liệu ra
# Một dòng gồm 3 số theo thứ tự là số tờ 5.000, số tờ 2.000 và số tờ 1.000 cách nhau 1
# dấu cách.
def number_of_5k(n):
    return n // 5000
def number_of_2k(n):
    return n // 2000
def number_of_1k(n):
    return n // 1000
n = int(input())
a = number_of_5k(n)
n_after =  n - 5000 * number_of_5k(n)
b = number_of_2k(n_after)
n_after = n_after - 2000 * number_of_2k(n_after)
print(f"{a} {b} {n_after}")