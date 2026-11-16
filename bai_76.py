# 0076 - Đếm số lần xuất hiện chuỗi c trong xâu
# Đề bài
# Viết chương trình nhập vào 1 xâu s1. Đếm xem xâu s2 xuất hiện trong xâu s1 bao
# nhiêu lần
# Dữ liệu vào
# Dòng 1 chứa xâu s1, dòng 2 chứa xâu s2.
# Dữ liệu ra
# Số lần xuất hiện của xâu s2 trong s1
s1 = input()
s2 = input()
count = 0
if len(s2) == 1:
    for i in range(len(s1)):
        if s1[i] == s2:
            count += 1
elif len(s2) != 1:
    s1 = s1.split()
    for j in range(len(s1)):
        if s1[j] == s2:
            count += 1
print(count)