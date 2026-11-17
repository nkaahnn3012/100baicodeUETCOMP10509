# 0083 - Đếm sô ký tự thường trong xâu
# Đề bài
# Viết chương trình nhập vào 1 xâu s. Đếm xem trong xâu có bao nhiêu ký tự thường
# Dữ liệu vào
# Chứa chuỗi s
# Dữ liệu ra
# Số lượng chữ in thường trong s
s = input()
count_upper = 0
count_space = 0
for i in range(len(s)):
    if s[i].isalpha() and s[i].upper() == s[i]:
        count_upper += 1
    elif s[i] == " ":
        count_space += 1
print(len(s) - count_upper - count_space)
