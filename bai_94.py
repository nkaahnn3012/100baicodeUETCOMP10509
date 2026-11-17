# 0094 - Viết hàm cộng trừ nhân chia 2 phân số
# Đề bài
# Viết chương trình nhập vào 2 phân số. Thực hiện cộng trừ nhân chia 2 phân số đã
# nhập, nếu kết quả là phân số lớn hơn 1 thì hiển thị bằng hỗn số, ngược lại kết quả là
# phân số tối giản.
# Dữ liệu vào
# Gồm 2 dòng, mỗi dòng có 2 số cách nhau bởi dấu cách theo thứ tự là tử số và mẫu số
# Dữ liệu ra
# Gồm 4 phân số theo thứ tự là kết quả +, -, *, /; nằm trên 4 dòng theo định dạng: tử/mẫu,
# nếu là hổn số thì in theo dạng: phần nguyên,tử/mẫu
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return (a * b) // gcd(a, b)
    
tu1, mau1 = map(int,input().split())
tu2, mau2 = map(int, input().split())

tu_add = tu1 * (lcm(mau1, mau2) // mau1) + tu2 * (lcm(mau1, mau2) // mau2)
mau_add = lcm(mau1, mau2)
gcd_add = gcd(tu_add, mau_add)
tu_add //= gcd_add
mau_add //= gcd_add

tu_sub = tu1 * (lcm(mau1, mau2) // mau1) - tu2 * (lcm(mau1, mau2) // mau2)
mau_sub = lcm(mau1, mau2)
gcd_sub = gcd(tu_sub, mau_sub)
tu_sub //= gcd_sub
mau_sub //= gcd_sub

tu_mul = tu1 * tu2
mau_mul = mau1 * mau2
gcd_mul = gcd(tu_mul, mau_mul)
tu_mul //= gcd_mul
mau_mul //= gcd_mul

tu_div = tu1 * mau2
mau_div = mau1 * tu2
gcd_div = gcd(tu_div, mau_div)
tu_div //= gcd_div
mau_div //= gcd_div

if tu_add / mau_add > 1:
    nguyen_add = tu_add // mau_add
    tu_add1 = tu_add - nguyen_add * lcm(mau1, mau2)
    print(f"{nguyen_add},{tu_add1}/{mau_add}")
else:
    print(f"{tu_add}/{mau_add}")

if tu_sub / mau_sub > 1:
    nguyen_sub = tu_sub // mau_sub
    tu_sub1 = tu_sub - nguyen_sub * lcm(mau1, mau2)
    print(f"{nguyen_sub},{tu_sub1}/{mau_sub}")
else:
    print(f"{tu_sub}/{mau_sub}")

if tu_mul / mau_mul > 1:
    nguyen_mul = tu_mul // mau_mul
    tu_mul1 = tu_mul - nguyen_mul * mau_mul
    print(f"{nguyen_mul},{tu_mul1}/{mau_mul}")
else:
    print(f"{tu_mul}/{mau_mul}")

if tu_div / mau_div > 1:
    nguyen_div = tu_div // mau_div
    tu_div1 = (tu_div - nguyen_div * mau_div)
    print(f"{nguyen_div},{tu_div1}/{mau_div}")
else:
    print(f"{tu_div}/{mau_div}")

