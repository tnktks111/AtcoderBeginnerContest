N, M = map(int, input().split())

def combination(n:int, m:int):
    res = []
    def dfs(idx:int, len:int, prev:int, limit:int, cur:list):
        if idx == len:
            res.append(tuple(cur))
            return
        for nxt in range(prev + 1, limit + 1):
            cur.append(nxt)
            dfs(idx + 1, len, nxt, limit, cur)
            cur.pop()
    dfs(0, n, 0, m, [])
    return res

res = combination(N, M)
for i in range(len(res)):
    print(*res[i])