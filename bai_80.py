# 0080 - Tìm vị trí đầu tiên mà ký tự x xuất hiện
# Đề bài
# Viết chương trình nhập vào 1 xâu s. Tìm vị trí đầu tiên mà ký tự x xuất hiện
# Dữ liệu vào
# Dòng 1 chứa chuỗi s, dòng 2 chứa chuỗi x.
# Dữ liệu ra
# Vị trí đầu tiên chuỗi x xuất hiện trong chuỗi s, nếu không có thì in số -1
s = input()
x = input()
s_have_x = False
for i in range(len(s)):
    if s[i] == x:
        s_have_x = True
        print(i)
        break
if s_have_x == False:
    print("-1")