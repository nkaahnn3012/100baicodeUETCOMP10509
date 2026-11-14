# 0066 - Xoá các khoảng trắng thừa ở đầu câu
# Đề bài
# Viết chương trình nhập vào 1 xâu. Xoá các khoảng trắng thừa ở đầu câu
# Vd: s= ‘└┘└┘└┘└┘vinh kim ’ -->s= ‘vinh kim ’
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s
# Dữ liệu ra
# Chuỗi s sau khi xoá khoảng trắng thừa ở đầu
s = input()
length = len(s)
count_space = 0
for i in range(length):
    if s[i] == " ":
        count_space += 1
    else:
        break
for j in range(count_space, length):
    print(s[j], end = "")
print()