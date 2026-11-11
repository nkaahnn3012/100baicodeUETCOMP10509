# 0016 - Xếp loại học sinh
# Đề bài
# Viết chương trình nhập vào điểm trung bình học kỳ I và trung bình học kỳ II, tính trung
# bình cả năm theo công thức: TBCN=(TBHKI+TBHKII*2)/3. Xếp lọai theo cách:
# “Gioi” nếu TBCN>=8
# “Kha” nếu 6.5<=TBCN <8
# “Trung binh” nếu 5.0<=TBCN <6.5
# “Yeu” nếu 3.5<=TBCN <5
# “Kem” nếu TBCN<3.5
# Dữ liệu vào
# Một dòng có 2 số thực cách nhau bởi dấu cách theo thứ tự là TBHKI và TBHKII
# Dữ liệu ra
# Dòng đầu là TBCN, làm tròn đến 1 chữ số thập phân; dòng thứ hai là xếp loại
a, b = map(float, input().split())
tbcn = (a + b * 2)/3
if tbcn >= 8:
    print(f"{tbcn:.1f}")
    print("Gioi")
elif 6.5 <= tbcn < 8:
    print(f"{tbcn:.1f}")
    print("Kha")
elif 5.0 <= tbcn < 6.5:
    print(f"{tbcn:.1f}")
    print("Trung binh")
elif 3.5 <= tbcn < 5:
    print(f"{tbcn:.1f}")
    print("Yeu")
else:
    print(f"{tbcn:.1f}")
    print("Kem")