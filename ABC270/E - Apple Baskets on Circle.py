N, K = map(int, input().split())
A = list(map(int, input().split()))
A_sort = sorted(A)

eaten = 0
eat_per_basket = 0
cur = 0
if sum(A) == K:
    print(*([0] * N)) 
    exit()
while True:
    nxt = (A_sort[cur] - eat_per_basket) * (N - cur)
    if eaten + nxt > K:
        break
    eaten += nxt
    eat_per_basket = A_sort[cur]
    cur += 1
last_eat_per_busket = (K - eaten) // (N - cur)
eaten += last_eat_per_busket * (N - cur)
eat_per_basket += last_eat_per_busket
finished = (eaten == K)
for i in range(N):
    if A[i] <= eat_per_basket:
        A[i] = 0
    elif not finished:
        A[i] -= (eat_per_basket + 1)
        eaten += 1
        if (eaten == K):
            finished = True
    else:
        A[i] -= eat_per_basket
print(*A)