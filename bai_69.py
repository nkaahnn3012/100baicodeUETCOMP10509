# 0069 - Đếm số từ trong câu
# Đề bài
# Viết chương trình nhập vào 1 xâu. Đếm xem trong xâu đó có bao nhiêu từ
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s.
# Dữ liệu ra
# Số từ trong câu
s = input()
s_after = []
count_space = 0
length = len(s)
for i in range(length - 1):
    if s[i] != " ":
        s_after.append(s[i])
    elif s[i] == " " and s[i + 1] != " ":
        s_after.append(s[i])
s_after.append(s[length - 1])
if s_after[0] == " ":
    for k in range(1, len(s_after)):
        if s_after[k] == " ":
            count_space += 1
else:
    for j in range(len(s_after)):
        if s_after[j] == " ":
            count_space += 1
print(count_space + 1)