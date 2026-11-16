# 0079 - Tìm ký tự xuất hiện nhiều lần nhất trong xâu
# Đề bài
# Viết chương trình nhập vào 1 xâu s. Tìm ký tự xuất hiện nhiều lần nhất trong xâu
# (không phân biệt chữ in hay thường, không tính khoảng trắng, nếu có nhiều ký tự xuất
# hiện nhiều nhất thì lấy ký tự đầu tiên tính từ trái sang)
# Dữ liệu vào
# Chứa chuỗi s
# Dữ liệu ra
# Chữ cái, dấu “:” và số lần xuất hiện trên cùng một dòng
s = input()
s = s.lower()
raw = []
for c in s:
    if c not in raw:
        raw.append(c)
freque = [0] *  len(raw)
for i in range(len(s)):
    for j in range(len(raw)):
        if s[i] == raw[j]:
            freque[j] += 1
max_freque = freque[0]
index = 0
for k in range(len(freque)):
    if freque[k] > max_freque:
        max_freque = freque[k]
        index = k
print(f"{raw[index]}:{max_freque}")