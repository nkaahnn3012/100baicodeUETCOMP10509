# 0037 - Rút gọn phân số.
# Đề bài
# Viết chương trình rút gọn phân số có tử là t và mẫu là m nguyên dương.
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng theo thứ tự là tử và mẫu của 1 phân số,
# cách nhau bởi dấu cách.
# Dữ liệu ra
# Phân số đã rút gọn theo thứ tự tử và mẫu cách nhau bởi dấu /
m, n = map(int, input().split())
list_m = []
list_n = []
list_mn = []
for i in range(2, m + 1):
    if m % i == 0:
        list_m.append(i)
for j in range(2, n + 1):
    if n % j == 0:
        list_n.append(j)
for u in range(len(list_m)):
        if list_m[u] in list_n:
            list_mn.append(list_m[u])
length = len(list_mn)
if m % n == 0:
    print(f"{m//n}/1")
elif n % m == 0:
    print(f"1/{n//m}")
else:
    mat = m // list_mn[length - 1]
    nat = n // list_mn[length - 1]
    print(f"{mat}/{nat}")