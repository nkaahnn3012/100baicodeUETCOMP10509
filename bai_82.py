# 0082 - Đếm ký tự in hoa trong xâu
# Đề bài
# Viết chương trình nhập vào 1 xâu s. Đếm xem trong xâu có bao nhiêu ký tự in hoa
# Dữ liệu vào
# Chứa chuỗi s.
# Dữ liệu ra
# Số lượng chữ in hoa trong s
s = input()
count_upper = 0
for i in range(len(s)):
    if s[i].isalpha() and s[i].upper() == s[i]:
        count_upper += 1
print(count_upper)
