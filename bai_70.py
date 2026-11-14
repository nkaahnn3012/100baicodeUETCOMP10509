# 0070 - Đổi ký tự đầu từ thành chữ in hoa
# Đề bài
# Viết chương trình nhập vào 1 xâu. Đổi ký tự đầu từ thành chữ in hoa
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s
# Dữ liệu ra
# Xâu đã chuyển đổi
s = input()
s_first = []
length = len(s)
if s[0].isalpha():
    print(chr(ord(s[0]) - 32), end = "")
for i in range (1, length):
    if (s[i].isalpha()) and (not s[i - 1].isalpha()):
        print(chr(ord(s[i]) - 32), end = "")
    else:
        print(s[i], end = "")
print()
