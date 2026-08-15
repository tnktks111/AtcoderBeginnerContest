# pythonのシフト演算は符号維持
N = int(input())
if (N >> 31) == 0 or (N >> 31) == -1:
    print("Yes")
else:
    print("No")