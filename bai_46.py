# 0046 - Tìm số x trong mảng
# Đề bài
# Viết chương trình nhập vào 1 mảng số nguyên có n phần tử. Nhập vào 1 số nguyên x.
# Tìm xem trong mảng có giá trị x hay không? Nếu có thì nó ở vị trí nào? (chỉ ra vị trí đầu
# tiên tìm thấy) vd: 2 3 1 4 1; x=1 có ở vị trí 2; x= 8 làkhông có.
# Dữ liệu vào
# Dòng 1 gồm 2 số nguyên dương n và x cách nhau bởi dấu cách, dòng 2 là n số
# nguyên.
# Dữ liệu ra
# Yes nếu x có trong a và vị trí của x nằm trên 2 dòng, hoặc No
n, x = map(int,input().split())
number = list(map(int,input().split()))
number_x = 0
index = 0
for i in range(n):
    if number[i] == x:
        number_x += 1
        index = i
        break
if number_x == 0:
    print("No")
else:
    print("Yes")
    print(index)