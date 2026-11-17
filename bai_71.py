# 0071 - Tìm kiếm và thay thế trong chuỗi
# Đề bài
# Viết chương trình thay thế tất cả các từ x trong một chuỗi s thành từ y.Vd: s= ‘anh co
# biet la em rat ghet anh lam khong?’; x= ‘anh’; y= ‘em’ -->s= ‘em co biet la em rat ghet
# em lam khong?’
# Dữ liệu vào
# Dòng 1 chứa chuỗi s, dòng 2 chứa chuỗi x, dòng 3 chứa chuỗi y
# Dữ liệu ra
# Xâu đã thay thế
s = input()
x = input()
y = input()
length_s, length_x, length_y = len(s), len(x), len(y)
if length_x != 1:
    s_after = list(s.split())
    for i in range(len(s_after)):
        if s_after[i] == x:
            s_after[i] = y
    print(*s_after, sep = " ")
elif length_x == 1:
    s_after = list(s)
    if length_x == 1:
        for i in range(length_s):
            if s[i] == x:
                s_after[i] = y
            else:
                s_after[i] = s[i]
        print("".join(s_after))

            
