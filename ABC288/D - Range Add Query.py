N, K = map(int, input().split())
A = list(map(int, input().split()))
A_cumsum_modK = [[0] * (N // K + 1) for _ in range(K)]
for i in range(N):
    A_cumsum_modK[i % K][i // K] += A[i]
    if i // K > 0:
        A_cumsum_modK[i % K][i // K] += A_cumsum_modK[i % K][i // K - 1]
Q = int(input())
# print(A_cumsum_modK)

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ok = True
    s = A_cumsum_modK[0][r // K] - A_cumsum_modK[0][(l - 1) // K] if l != 0 else A_cumsum_modK[0][r // K]
    # print(s)
    for i in range(1, K):
        if not ok:
            continue
        if l == 0:
            A_left = 0
        else:
            left = (l - 1) // K if (l - 1) % K >= i else (l - 1) // K - 1
            A_left = A_cumsum_modK[i][left]
        if r % K >= i:
            right = r // K
            A_right = A_cumsum_modK[i][right]
        elif r // K > 0:
            right = r // K - 1
            A_right = A_cumsum_modK[i][right]
        else:
            A_right = 0
        if A_right - A_left != s:
            ok = False
            print("No")
            # print(f"No at i = {i}, tmp = {A_right - A_left}")
    if ok:
        print("Yes")