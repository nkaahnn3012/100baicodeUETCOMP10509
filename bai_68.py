# 0068 - Xoá các khoảng trắng thừa ở giữa câu
# Đề bài
# Viết chương trình nhập vào 1 xâu. Xoá các khoảng trắng thừa ở giữa câu
# Vd: s=‘ vinh└┘└┘└┘└┘└┘kim ’
# --> s=‘ vinh kim ’
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s.
# Dữ liệu ra
# Chuỗi s sau khi xoá khoảng trắng thừa ở giữa câu
s = input()
s_after = []
length = len(s)
for i in range(length - 1):
    if s[i] != " ":
        s_after.append(s[i])
    elif s[i] == " " and s[i + 1] != " ":
        s_after.append(s[i])
s_after.append(s[length - 1])
for j in range(len(s_after)):
    print(s_after[j], end = "")
print()