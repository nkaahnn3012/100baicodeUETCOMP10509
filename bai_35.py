# 0035 - Tính trung bình cộng các số nguyên tố từ m đến n
# Đề bài
# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Tính trung bình cộng các số
# nguyên tố từ m đến n. Nếu không có số nào thì in dấu -
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách.
# Dữ liệu ra
# Là trung bình cộng các số nguyên tố từ m đến n, làm tròn đến 2 chữ số thập phân
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
    tbc = round(sum(list) / len(list), 2)
    print(tbc)