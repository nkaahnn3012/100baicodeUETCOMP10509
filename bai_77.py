# 0077 - Đếm số ký tự khác nhau trong xâu
# Đề bài
# Viết chương trình nhập vào 1 xâu s. Đếm xem trong xâu s có bao nhiêu ký tự khác
# nhau
# Dữ liệu vào
# Chứa chuỗi s
# Dữ liệu ra
# Số lượng ký tự khác nhau trong xâu
# s = input()
# freque = [True] * (len(s))
# for i in range (len(s)):
#     for j in range(len(s) - 1 - i):
#         if s[i] == s[i + j + 1]:
#             freque[i + j + 1] = False
#             break
# count = 0
# for k in range(len(s)):
#     if freque[k] == True:
#         count += 1
# print(count)
# print(freque)
s = input()
s1 = []
for c in s:
    if c not in s1:
        s1.append(c)
print(len(s1)) 