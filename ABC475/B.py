N = int(input())
A = list(map(int, input().split()))

cnt = [0, 0, 0] # 100, 10, 1

for i in range(N):
    p, q = divmod(A[i], 1000)
    if q:
        p += 1
    remain = 1000 * p - A[i]
    # print(remain)
    hundred, remain = divmod(remain, 100)
    tens, remain = divmod(remain, 10)
    cnt[2] += hundred
    cnt[1] += tens
    cnt[0] += remain

print(*cnt)