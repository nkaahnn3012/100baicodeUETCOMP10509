# 0088 - Viết hàm tìm UCLN
# Đề bài
# Viết chương trình con tìm UCLN của 2 số nguyên a, b; Sau đó sử dụng chương trình
# con này để rút gọn phân số có tử và mẫu là nhũng số nguyên.
# Dữ liệu vào
# Hai số nguyên dương m và n trên cùng 1 dòng theo thứ tự là tử và mẫu của 1 phân số,
# cách nhau bởi dấu cách.
# Dữ liệu ra
# Phân số đã rút gọn theo thứ tự tử và mẫu cách nhau bởi dấu /
def gcd(a, b):
    div_a = []
    div_b = []
    div_ab = []
    for i in range(1, a + 1):
        if a % i == 0:
            div_a.append(i)
    for j in range(1, b + 1):
        if b % j == 0:
            div_b.append(j)
    for k in range(len(div_a)):
        if div_a[k] in div_b:
            div_ab.append(div_a[k])
    return(max(div_ab))
a, b = map(int, input().split())
tso = int(a / gcd(a, b))
mso = int(b / gcd(a, b))
print(f"{tso}/{mso}")