# 0036 - Tìm UCLN của 2 số nguyên dương a, b
# Đề bài
# Tìm UCLN của 2 số nguyên dương a, b
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách
# Dữ liệu ra
# Ước chung lớn nhất của m và n.
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
    print(n)
elif n % m == 0:
    print(m)
else:
    print(list_mn[length - 1])
