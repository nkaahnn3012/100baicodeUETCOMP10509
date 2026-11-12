# 0033 - Đếm số nguyên tố từ m đến n
# Đề bài
# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Đếm xem trong các số nguyên
# từ m đến n, có bao nhiêu số nguyên tố
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách
# Dữ liệu ra
# Số lượng số nguyên tố từ m đến n
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
number = 0
for i in range(m, n+1):
    if is_prime(i):
        number += 1
print(number)