# 0031 - Đếm số chia hết cho 3 từ m đến n
# Đề bài
# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Đếm xem trong các số nguyên
# từ m đến n, có bao nhiêu số chia hết cho 3
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách
# Dữ liệu ra
# Số lượng số chia hết cho 3 từ m đến n
m, n = map(int,input().split())
list = []
for i in range(m,n+1):
    if i % 3 == 0:
        list.append(i)
print(len(list))
