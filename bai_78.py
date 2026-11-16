# 0078 - Mỗi ký tự xuất hiện bao nhiêu lần trong xâu
# Đề bài
# Viết chương trình nhập vào 1 xâu s. Đếm xem trong xâu s mỗi ký tự xuất hiện bao
# nhiêu lần (không phân biệt chữ in hay thường, đếm cả khoảng trắng )
# Dữ liệu vào
# Chứa chuỗi s
# Dữ liệu ra
# Chữ cái, dấu “:” và số lần xuất hiện, dấu cách, chữ cái tiếp theo,… trên cùng một dòng
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
for k in range(len(raw)):
    print(f"{raw[k]}:{freque[k]}", end = " ")
print()