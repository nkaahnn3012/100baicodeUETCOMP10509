# 0090 - Viết hàm P(x,n) để tính giá trị x^n.
# Đề bài
# Áp dụng tính: F(x) = a1.x^n1+ a2.x^n2+ a3.x^n3… +ak.x^nk.
# Dữ liệu vào
# Dòng 1 là 2 số nguyên k và x cách nhau một dấu cách; k dòng tiếp theo, mỗi dòng gồm
# 2 số theo thứ tự là ak và nk
# Dữ liệu ra
# Giá trị của F(x)
def power(x, n):
    if n == 0:
        return 1
    elif n != 0:
        return x * power(x, n - 1)
k, x = map(int, input().split())
a_list = []
n_list = []
for i in range(k):
    a, n = map(int,input().split())
    a_list.append(a)
    n_list.append(n)
fx_comp = []
for j in range(k):
    comp = a_list[j] * power(x, n_list[j])
    fx_comp.append(comp)
print(sum(fx_comp))
