# 0019 - Tính số nút của biển số xe
# Đề bài
# Nhập vào số xe (có năm chữ số) trong biển số xe máy của bạn. Cho biết số xe của bạn
# được mấy nút. Bạn là người may mắn nếu số nút=9. Bạn có may mắn không?
# Ví dụ: số xe là 45046, tổng các chữ số là 4+ 5 +0+ 4 + 6 = 19 thì 19 mod 10 =9. Số nút
# là 9: may man. Số xe 12340, tổng các chữ số là 1+2+3+4+0=10 thì 10 mod 10=0. Số
# nút là 0: chua may man
# Dữ liệu vào
# Một số nguyên x có 5 chữ số
# Dữ liệu ra
# Dòng 1 là số nút, dòng 2 là “may man” hoặc “chua may man”
def sum_digit(x):
    sum = 0
    for i in range (5):
        sum += (x % 10)
        x = x // 10
    return sum
x = int(input())
sum = sum_digit(x)
nut = sum % 10
if nut == 9:
    print(nut)
    print("may man")
else:
    print(nut)
    print("chua may man")
