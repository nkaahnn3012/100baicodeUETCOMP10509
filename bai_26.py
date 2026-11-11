# 0026 - Tính tổng những số chia hết cho 3 và 5
# Đề bài
# Viết chương trình nhập vào 1 số nguyên dương n. Tính tổng những số chia hết cho 3
# và 5 từ 1 đến n
# Dữ liệu vào
# Một số nguyên dương n
# Dữ liệu ra
# Tổng các số chia hết cho 3 và 5 từ 1 đến n
def sum_of_list(list):
    return sum(list)
n = int(input())
list_15 = []
for i in range (1, n+1):
    if i % 15 == 0:
        list_15.append(i)
tong_can_tinh = sum_of_list(list_15)
print(f"{tong_can_tinh}")
