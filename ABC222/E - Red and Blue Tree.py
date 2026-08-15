from collections import deque

MOD = 998244353

N, M, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

adj = [[] for _ in range(N)]
tuple2idx = dict()
for i in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)
    tuple2idx[(u, v)] = i
    tuple2idx[(v, u)] = i

cnts = [0] * (N - 1)

def cnt_edge_from_u_to_v(u:int, v:int):
    parents = [-1] * N
    
    q = deque([u])
    seen = set()
    while q:
        cur = q.popleft()
        if cur in seen:
            continue
        if cur == v:
            break
        for nei in adj[cur]:
            if nei == parents[cur]:
                continue
            if nei in seen:
                continue
            parents[nei] = cur
            q.append(nei)

    cur = v
    while cur != u:
        cnts[tuple2idx[(cur, parents[cur])]] += 1
        cur = parents[cur]

for i in range(M - 1):
    cnt_edge_from_u_to_v(A[i], A[i + 1])

# print(cnts)

L = sum(cnts)
if L % 2 != K % 2 or L + K < 0 or L - K < 0:
    print(0)
    exit()

R_cnts = (L + K) // 2
B_cnts = (L - K) // 2

def solve_cnt(cnts:list[int], R_cnts: int):
    non_zeros = []
    for c in cnts:
        if c != 0:
            non_zeros.append(c)
    
    # print(non_zeros)
    # print(R_cnts)
    length = len(non_zeros)
    
    dp = [0] * (R_cnts + 1)
    dp[0] = 1
    
    for i in range(1, length + 1):
        next_dp = [0] * (R_cnts + 1)
        for j in range(R_cnts + 1):
            next_dp[j] += dp[j]
            next_dp[j] %= MOD
            if j + non_zeros[i - 1] <= R_cnts:
                next_dp[j + non_zeros[i - 1]] += dp[j]
                next_dp[j] %= MOD
        dp = next_dp
    
    res = dp[R_cnts]
    for _ in range(N - 1 - length):
        res = (res * 2) % MOD
    return res

print(solve_cnt(cnts, R_cnts))