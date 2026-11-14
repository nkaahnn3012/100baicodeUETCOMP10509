# 0062 - Viết xâu theo thứ tự ngược lại.
# Đề bài
# Viết chương trình nhập vào 1 xâu, đưa ra xâu đó viết theo thứ tự ngược lại.
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s.
# Dữ liệu ra
# Chuỗi s viết theo thứ tự ngược lại
s  = input()
for i in range(len(s)):
    print(f"{s[len(s) - i -1]}", end = "")
print()