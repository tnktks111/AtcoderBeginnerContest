import sys
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())

res = []
def dfs(idx:int, cur:list, cur_sum:int):
    if idx == 2:
        for i in range((K - cur_sum) // 2 + 1):
            cur.append(i)
            cur.append(K - cur_sum - i * 2)
            res.append(tuple(cur[::-1]))
            cur.pop()
            cur.pop()
        return

    elif idx == 1:
        cur.append(K - cur_sum)
        res.append(tuple(cur[::-1]))
        cur.pop()
        return

    a = 0
    while True:
        if cur_sum + a * idx > K:
            break
        cur.append(a)
        dfs(idx - 1, cur, cur_sum + a * idx)
        cur.pop()
        a += 1

dfs(N, [], 0)
res.sort()

for r in res:
    print(*r)
