# 0087 - Viết hàm kiểm tra chia hết cho 5
# Đề bài
# Viết chương trình con kiểm tra 1 số nguyên nhập từ bàn phím có chia hết cho 5 hay
# không?
# Dữ liệu vào
# Một số nguyên n.
# Dữ liệu ra
# Yes nếu n là số chia hết cho 5; No nếu n là số không chia hết cho 5   
def multiple_5 (a):
    if a % 5 == 0:
        return True
    else:
        return False
n = int(input())
if multiple_5(n):
    print("Yes")
else:
    print("No")