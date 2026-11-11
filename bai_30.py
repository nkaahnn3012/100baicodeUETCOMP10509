# 0030 - Tính tổng các số nguyên từ m đến n
# Đề bài
# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Tính tổng các số nguyên từ m
# đến n
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách
# Dữ liệu ra
# Tổng các số nguyên từ m đến n
m, n = map(int, input().split())
number = (n - m) + 1
sum = (m + n) * number // 2
print(sum)