from bisect import bisect_left

Q = int(input())
S = input()
T = input()

s_len = len(S)
t_len = len(T)
starts = []
for i in range(s_len - t_len + 1):
    if S[i:i+t_len] == T:
        starts.append(i)

# print(starts)
for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    idx = bisect_left(starts, l)
    if idx == len(starts):
        print("No")
    else:
        # print(l, r, idx)
        if starts[idx] + t_len - 1 <= r:
            print("Yes")
        else:
            print("No")
