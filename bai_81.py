# 0081 - Tìm vị trí cuối mà ký tự x xuất hiện trong xâu
# Đề bài
# Viết chương trình nhập vào 1 xâu s. Tìm vị trí cuối mà ký tự x xuất hiện
# Dữ liệu vào
# Dòng 1 chứa chuỗi s, dòng 2 chứa chuỗi x
# Dữ liệu ra
# Vị trí cuối cùng chuỗi x xuất hiện trong chuỗi s, nếu không có thì in số -1
s = input()
x = input()
index = -1
for i in range(len(s)):
    if s[i] == x:
        index = i
print(index)