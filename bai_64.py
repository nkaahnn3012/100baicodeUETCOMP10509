# 0064 - Xoá bỏ các dấu cách trong chuỗi
# Đề bài
# Viết chương trình nhập vào 1 xâu, đưa ra xâu đó sau khi đã loại bỏ các dấu cách.
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s
# Dữ liệu ra
# Chuỗi s đã loại bỏ khoảng trắng
s = input()
for i in range(len(s)):
    if s[i] != " ":
        print(f"{s[i]}", end = "")
print()