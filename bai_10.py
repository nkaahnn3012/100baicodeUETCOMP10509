# 0010 - Chia táo
# Đề bài
# Viết chương trình nhập vào số học sinh của 1 lớp (HS) và số táo trong rổ (T). Hãy chia
# đều số táo cho tất cả học sinh trong lớp, mỗi bạn sẽ được bao nhiêu quả táo? Còn dư
# lại bao nhiêu quả?
# Dữ liệu vào
# Gồm 1 dòng có 2 số nguyên cách nhau bởi dấu cách theo thứ tự là T và HS
# Dữ liệu ra
# Là số táo mỗi học sinh được chia và tổng số táo còn dư, các số cách nhau bởi dấu
# cách
t, hs = map(int, input().split())
so_tao_duoc_nhan = t // hs
so_tao_du = t % hs
print(so_tao_duoc_nhan, so_tao_du)