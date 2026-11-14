# 0067 - Xoá các khoảng trắng thừa ở cuối câu
# Đề bài
# Viết chương trình nhập vào 1 xâu. Xoá các khoảng trắng thừa ở cuối câu
# Vd: s=‘ vinh kim└┘└┘└┘└┘’
# --> s=‘ vinh kim’
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s.
# Dữ liệu ra
# Chuỗi s sau khi xoá khoảng trắng thừa ở cuối
# (Dấu + trong test mẫu là ký hiệu khoảng trắng)
s = input()
length = len(s)
count_space_end = 0
for i in range(length):
    if s[length - 1 - i] == " ":
        count_space_end += 1
    else:
        break
for j in range(0, length - count_space_end):
    print(s[j], end = "")
print()
print(count_space_end)