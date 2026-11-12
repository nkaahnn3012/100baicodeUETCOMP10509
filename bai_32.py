# 0032 - Đếm số chia hết cho 3 hoặc chia hết cho 5 và tính
# tổng các số chẵn
# Đề bài
# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Đếm xem trong các số nguyên
# từ m đến n, có bao nhiêu số chia hết cho 3 hoặc chia hết cho 5. Tính tổng các số chẵn.
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách
# Dữ liệu ra
# Một dòng có 2 số, số thứ nhất là số lượng số chia hết cho 3 hoặc 5 từ m đến n, số thứ
# 2 là tổng các số chẵn từ m đến n, hai số cách nhau bởi dấu cách
m, n = map(int, input().split())
list_3 = []
list_5 = []
list_15 = []
for i in range (m, n+1):
    if i % 3 == 0:
        list_3.append(i)
for i in range (m, n+1):
    if i % 5 == 0:
        list_5.append(i)
for i in range (m, n+1):
    if i % 15 == 0:
        list_15.append(i)
number = len(list_3) + len(list_5) - len(list_15)
if ((m % 2 == 0) and (n % 2 == 1)) or ((m % 2 == 1) and (n % 2 == 0)):
    a = ((n - m - 1) // 2) + 1
    sum = (m + n - 1) * a // 2   
elif m % 2 == 0 and n % 2 == 0:
    a = ((n - m) // 2) + 1
    sum = (m + n) * a // 2
elif m % 2 == 1 and n % 2 == 1:
    a = ((n - m - 2) // 2) + 1
    sum = (m + n) * a // 2
print(f"{number} {sum}")
    