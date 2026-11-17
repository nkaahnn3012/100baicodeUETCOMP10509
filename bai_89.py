# 0089 - Viết hàm tính n!
# Đề bài
# Viết chương trình con để tính n! = 1.2...n. Áp dụng tính tổng m biểu thức với
# Dữ liệu vào
# Dòng 1 là số nguyên m; m dòng tiếp theo, mỗi dòng gồm 2 số theo thứ tự là n và k
# Dữ liệu ra
# Tổng của m biểu thức trên
def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
     return n * factorial(n - 1)

n_list = []
k_list = []

m = int(input())
for i in range(m):
   n, k = map(int,input().split())
   n_list.append(n)
   k_list.append(k)

nCk = []
for j in range(m):
   a = factorial(n_list[j]) // (factorial(k_list[j]) * factorial(n_list[j] - k_list[j]))
   nCk.append(a)
print(sum(nCk))
