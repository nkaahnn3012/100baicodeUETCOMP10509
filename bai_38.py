# 0038 - In ra k số nguyên tố đầu tiên
# Đề bài
# Viết chương trình nhập vào số nguyên dương k, in ra k số nguyên tố đầu
# tiên.
# Dữ liệu vào
# Một số nguyên dương k
# Dữ liệu ra
# Dãy k số nguyên tố đầu tiên, các số cách nhau bởi dấu cách
def is_prime(a):
    if a == 2:
        return True
    elif a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
k = int(input())
number_prime = 0
n = 2
list = []
while True:
    if number_prime == k:
        break
    else:
        if is_prime(n):
            list.append(n)
            number_prime += 1
        n += 1
for i in range(len(list)):
    print(list[i], end = " ")
print()
