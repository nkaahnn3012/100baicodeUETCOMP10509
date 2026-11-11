# 0018 - Tính số ngày của tháng
# Đề bài
# Viết chương trình nhập vào 1 tháng và năm, cho biết tháng đó có bao nhiêu ngày (Năm
# nhuận là năm chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100).
# Dữ liệu vào
# Hai số nguyên tháng và năm cách nhau bởi dấu cách
# Dữ liệu ra
# Kết quả tháng đó có bao nhiêu ngày
def is_leapyear(y):
    if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
        return True
m, y = map(int, input().split())
if is_leapyear(y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        print("31")
    elif m in [4, 6, 9, 11]:
        print("30")
    elif m == 2:
        print("29")
elif not is_leapyear(y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        print("31")
    elif m in [4, 6, 9, 11]:
        print("30")
    elif m == 2:
        print("28")
