# 0011 - Tính giờ phút giây
# Đề bài
# Viết chương trình nhập vào tổng số giây là một số nguyên, in ra giờ:phút:giây.
# Dữ liệu vào
# Một số nguyên là tổng số giây
# Dữ liệu ra
# Kết quả đổi được theo dạng giờ:phút:giây
def hours(s):
    return int(s / 3600)
def minutes(s, h):
    return int((s - 3600*h)/ 60)
s = int(input())
s_after = s - (3600 * hours(s)) - (60 * minutes(s, hours(s)))
print(hours(s), minutes(s, hours(s)), s_after, sep = ":")
