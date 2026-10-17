N, W = map(int, input().split())

tastes = []
volumes = []
for _ in range(N):
    a, b = map(int, input().split())
    tastes.append(a)
    volumes.append(b)

res = 0
for bit in range(1 << N):
    tmp_taste = 0
    tmp_vol = 0
    for i in range(N):
        if (1 << i) & bit:
            tmp_taste += tastes[i]
            tmp_vol += volumes[i]
    if tmp_vol > W:
        continue
    res = max(res, tmp_taste)

print(res)
