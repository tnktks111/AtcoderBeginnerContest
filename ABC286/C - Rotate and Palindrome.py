N, A, B = map(int, input().split())
S = input()

res = float("inf")
for i in range(N):
    tmp = A * i
    if res < tmp:
        break
    S_rotated = S[i:] + S[:i]
    # print(S_rotated)
    for j in range(N // 2):
        if S_rotated[j] != S_rotated[-j - 1]:
            tmp += B
    # print(tmp)
    res = min(res, tmp)
print(res)
