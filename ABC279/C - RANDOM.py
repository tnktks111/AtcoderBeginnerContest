from collections import Counter
H, W = map(int, input().split())
S = list(input() for _ in range(H))
T = list(input() for _ in range(H))
S_arr = list(zip(*S))
T_arr = list(zip(*T))
S_arr.sort()
T_arr.sort()
for i in range(W):
    if S_arr[i] != T_arr[i]:
        print("No")
        exit()
print("Yes")