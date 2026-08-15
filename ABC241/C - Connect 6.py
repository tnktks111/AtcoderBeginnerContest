N = int(input())
S = [input() for _ in range(N)]

ok = False
#よこ
for r in range(N):
    max_len = 0
    left = 0
    dots = 0
    for right in range(N):
        if S[r][right] == ".":
            dots += 1
        while dots > 2:
            if S[r][left] == ".":
                dots -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    if max_len >= 6:
        ok = True
        break
if ok:
    print("Yes")
    exit()
#たて
for c in range(N):
    max_len = 0
    left = 0
    dots = 0
    for right in range(N):
        if S[right][c] == ".":
            dots += 1
        while dots > 2:
            if S[right][c] == ".":
                dots -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    if max_len >= 6:
        ok = True
        break
if ok:
    print("Yes")
    exit()

#左上から右下
for k in range(2 * N - 1):
    diff = k - (N - 1) #r - c
    length = N - abs(diff)
    start = (0, -diff) if diff < 0 else (diff, 0)
    max_len = 0
    left = 0
    dots = 0
    for right in range(length):
        if S[start[0] + right][start[1] + right] == ".":
            dots += 1
        while dots > 2:
            if S[start[0] + left][start[1] + left] == ".":
                dots -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    if max_len >= 6:
        ok = True
        break
if ok:
    print("Yes")
    exit()
#左下から右上
for k in range(2 * N - 1):
    length = N - abs(k - (N - 1))
    start = (k, 0) if k < N else (N - 1, k - N + 1)
    max_len = 0
    left = 0
    dots = 0
    for right in range(length):
        if S[start[0] - right][start[1] + right] == ".":
            dots += 1
        while dots > 2:
            if S[start[0] - left][start[1] + left] == ".":
                dots -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    if max_len >= 6:
        ok = True
        break
if ok:
    print("Yes")
else:
    print("No")