# 0092 - Sử dụng hàm lồng nhau
# Đề bài
# Viết chương trình có 2 hàm có tham số: cộng a và b; chia a cho b. Trong chương trình
# chính sử dụng chương trình con để tính a+b+c va a/b+c và a/(b+c)
# Dữ liệu vào
# Gồm 1 dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c.
# Dữ liệu ra
# Gồm 3 số trên một dòng: số thứ nhất là kết quả của phép tính a+b+c (không có số thập
# phân), số thứ hai là kết quả củaphép tính a/b+c (làm tròn đến chữ số thập phân thứ 2),
# số thứ ba là kết quả của phép tính a/(b+c) (làm tròn đến chữ số thập phân thứ 3)
def add(a, b):
    return a + b
def divide(a, b):
    return a / b
a, b, c = map(int,input().split())
re1 = int(add(add(a, b), c))
re2 = add(divide(a, b), c)
re3 = divide(a, add(b, c))
print(f"{re1} {re2:.2f} {re3:.3f}")