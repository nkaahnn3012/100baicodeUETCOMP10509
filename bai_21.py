# 0021 - Tính tiền Taxi
# Đề bài
# Viết chương trình tính tiền taxi căn cứ vào đoạn đường đi, biết rằng
# 
#  1 km đầu giá 12000đ
#  km thứ 2 đến km thứ 30 giá 10000đ
#  km thứ 31 trở đi tính 9000đ
# Vd:
# + km=3 thìTien=1*12000+(3-1)*10000=12000+20000=32000
# + km=40 thì Tien=12000+29*10000+(40-30)*9000=392000
# Dữ liệu vào
# Một số nguyên n là số km đã đi.
# Dữ liệu ra
# Số tiền cần trả
n = int(input())
if n > 30:
    print(12000 + 29  * 10000 + (n - 30) * 9000)
elif n > 1:
    print(12000 + (n - 1) * 10000)
else:
    print("12000")