# 0065 - Kiểm tra xâu đối xứng
# Đề bài
# Viết chương trình nhập vào 1 xâu, kiểm tra xem xâu đó có đối xứng hay không?
# Vd:madam, tenet, 1234321; tim mit nhưng 12334321 là không đối xứng
# Dữ liệu vào
# Gồm 1 dòng chứa chuỗi s.
# Dữ liệu ra
# Yes nếu s là chuỗi đối xứng, No nếu s không phải đối xứng
s = input()
palindrome = True
for i in range(len(s)):
    if s[i] != s[len(s) -1 - i]:
        palindrome = False
if palindrome == True:
    print("Yes")
else:
    print("No")