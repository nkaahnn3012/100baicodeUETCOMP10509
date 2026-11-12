# 0034 - In các số nguyên tố từ m đến n
# Đề bài
# Viết chương trình nhập vào 2 số nguyên m và n (m<n). In các số nguyên tố từ m đến n.
# Nếu không có số nào thì in dấu -
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách
# Dữ liệu ra
# Gồm các số nguyên tố từ m đến n trên cùng một dòng, các số cách nhau 1 dấu cách
def is_prime(a):
    if a == 2:
        return True
    elif a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
m, n = map(int, input().split())
list = []
for i in range(m, n+1):
    if is_prime(i):
        list.append(i)
if len(list) == 0:
    print("-")
else:
    for j in range (len(list)):
        print(f"{list[j]}", end=" ")
    print()