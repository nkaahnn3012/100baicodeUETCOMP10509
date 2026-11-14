# 0063 - In xâu với mỗi ký tự trên 1 dòng
# Đề bài
# Viết chương trình nhập vào 1 xâu. In xâu đó với mỗi ký tự trên 1 dòng.
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s
# Dữ liệu ra
# Chuỗi s với mỗi ký tự trên 1 dòng
s = input()
for i in range(len(s)):
    print(f"{s[i]}")