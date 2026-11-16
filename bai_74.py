# 0074 - Đảo ngược các từ trong câu
# Đề bài
# Viết chương trình đảo ngược các từ trong câu vừa nhập. vd: tôi đi họcàhọc đi tôi.Vd: tôi
# đi học -->học đi tôi
# Dữ liệu vào
# Chứa chuỗi s gồm 1 câu
# Dữ liệu ra
# Xâu đảo theo yêu cầu
s = input()
s = s.split()
for i in range(len(s)):
    print(s[len(s) - 1 - i], end = " ")
print()