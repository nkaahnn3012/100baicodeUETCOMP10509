# 0085 - Tìm họ và chữ lót của một người từ chuỗi họ và tên
# Đề bài
# Viết chương trình nhập vào họ và tên của 1 người. In ra họ của người đó
# Dữ liệu vào
# Một dòng chứa chuỗi họ và tên của một người
# Dữ liệu ra
# Họ và chữ lót của người đó (Xoá tất cả các dấu cách thừa)
s = list(input().split())
for i in range(len(s) - 1):
    print(s[i], end = " ")
print()
