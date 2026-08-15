N, X = map(int, input().split())
jumps = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (X + 1) for _ in range(N + 1)]
dp[0][0] = 1
for r in range(1, N + 1):
    ok = False
    for c in range(X + 1):
        if dp[r - 1][c]:
            if c + jumps[r - 1][0] <= X:
                ok = True
                dp[r][c + jumps[r - 1][0]] += dp[r - 1][c] 
            if c + jumps[r - 1][1] <= X:
                ok = True
                dp[r][c + jumps[r - 1][1]] += dp[r - 1][c]
    if not ok:
        break
print("Yes" if dp[N][X] else "No") 


# bit全探索でやろうとしたが、当然timeout(2^n)
# N, X = map(int, input().split())
# jumps = [tuple(map(int, input().split())) for _ in range(N)]
# ok = False
# for i in range(1 << N):
#     position = 0
#     for j in range(N):
#         position += jumps[j][(i >> j) & 1]
#         if position > X:
#             break
#     if position == X:
#         ok = True
#         break
# print("Yes" if ok else "No")