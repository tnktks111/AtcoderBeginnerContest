N, K = map(int, input().split())

diff = []
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans += a
    diff.append(b - a)
    
# print(f"A sum = {ans}")
# print(f"diff = {diff}")

for _ in range(K):
    res = (-1, (-1, -1))
    
    l = 0
    r = 0
    while l < N:
        if diff[l] < 0:
            l += 1
            continue
        tmp = 0
        for r in range(l, N):
            tmp += diff[r]
            if tmp < 0:
                break
            if res[0] < tmp:
                res = (tmp, (l, r))
        if tmp < 0:
            l = r + 1
        else:
            break

    # print(f"res = {res}")
    if res[0] == -1:
        print(ans)
        exit()

    l, r = res[1]
    for i in range(l, r + 1):
        diff[i] *= -1
    
    ans += res[0]
    # print(f"diff = {diff}")
    # print(f"ans = {ans}")

print(ans)
