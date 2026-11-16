# 0075 - Đảo ngược các ký tự trong từng từ.
# Đề bài
# Viết chương trình đảo ngược các ký tự từng từ trong câu vừa nhập. vd: tôi đi học -->iot
# id coh
# Dữ liệu vào
# Chứa chuỗi s
# Dữ liệu ra
# Xâu đảo theo yêu cầu
s = input()
for i in range(len(s)):
    print(s[len(s) - 1 - i], end = "")
print()