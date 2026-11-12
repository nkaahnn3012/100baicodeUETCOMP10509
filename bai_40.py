# 0040 - In ra k số chính phương đầu tiên
# Đề bài
# Viết chương trình nhập vào số nguyên dương k, in ra k số chính phương đầu tiên
# Dữ liệu vào
# Một số nguyên dương k
# Dữ liệu ra
# Dãy k số chính phương đầu tiên, các số cách nhau bởi dấu cách
k = int(input())
list = []
for i in range (k):
    list.append(i ** 2)
for j in range (len(list)):
    print(list[j], end =" ")
print()