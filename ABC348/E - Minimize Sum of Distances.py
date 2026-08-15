N = int(input())

adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

C = list(map(int, input().split()))

dp1 = [[C[i], 0] for i in range(N)]

def recursive_dfs1(root:int):
    stack = [root]
    parent = [-1] * N
    seen = [False] * N

    while stack:
        cur = stack.pop()
        if seen[cur]:
            for nei in adj[cur]:
                if nei == parent[cur]:
                    continue
                dp1[cur][0] += dp1[nei][0]
                dp1[cur][1] += (dp1[nei][0] + dp1[nei][1])
        else:
            seen[cur] = True
            stack.append(cur)
            for nei in adj[cur]:
                if nei == parent[cur]:
                    continue
                parent[nei] = cur
                stack.append(nei)

recursive_dfs1(0)
ans = [0] * N
ans[0] = dp1[0][1]
total_weight = dp1[0][0]

def recursive_dfs2(root:int):
    stack = [root]
    parent = [-1] * N
    while stack:
        cur = stack.pop()
        for nei in adj[cur]:
            if nei == parent[cur]:
                continue
            parent[nei] = cur
            # sub重み和 + subスコア和
            # sub重み和 = 総重量 - 自重(total_weight - C[nei])
            # subスコア和 = 上subスコア和 + 下subスコア和
            # 上スコア和 = curを根とするスコア - 自分の寄与
            # 下スコア和 = 自スコア - (下subtreeの重み和)
            ans[nei] = (total_weight - C[nei]) + (ans[cur] - (dp1[nei][0] + dp1[nei][1])) + (dp1[nei][1] - (dp1[nei][0] - C[nei]))
            # ans[nei] = total_weight + ans[cur] - 2 * dp1[nei][0]
            stack.append(nei)

recursive_dfs2(0)
print(min(ans))