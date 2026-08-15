import sys
sys.setrecursionlimit(2 * 10 ** 5)

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(lambda x:int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp1 = [[1, 0] for _ in range(N)]

def dfs1(root:int, parent:int):
    for nei in adj[root]:
        if nei == parent:
            continue
        dfs1(nei, root)
        dp1[root][1] += sum(dp1[nei])
        dp1[root][0] += dp1[nei][0]

def iterative_dfs1(root:int):
    stack = [root]
    parent = [-1] * N
    visit = [False] * N
    while stack:
        cur = stack.pop()
        if visit[cur]:
            for nei in adj[cur]:
                if nei == parent[cur]:
                    continue
                dp1[cur][1] += (dp1[nei][0] + dp1[nei][1])
                dp1[cur][0] += dp1[nei][0]
        else:
            visit[cur] = True
            stack.append(cur)
            for nei in adj[cur]:
                if nei == parent[cur]:
                    continue
                stack.append(nei)
                parent[nei] = cur

dp2 = [[1, 0] for _ in range(N)]
def dfs2(root:int, parent:int):
    children = [nei for nei in adj[root] if nei != parent]
    
    acc_l = [[0, 0] for _ in range(len(children) + 1)]
    acc_r = [[0, 0] for _ in range(len(children) + 1)]
    
    for i in range(len(children)):
        child = children[i]
        acc_l[i + 1][0] = acc_l[i][0] + dp1[child][0]
        acc_l[i + 1][1] = acc_l[i][1] + sum(dp1[child])

    for i in range(len(children) - 1, -1, -1):
        child = children[i]
        acc_r[i][0] = acc_r[i + 1][0] + dp1[child][0]
        acc_r[i][1] = acc_r[i + 1][1] + sum(dp1[child])

    for i, child in enumerate(children):
        dp2[child][0] = acc_l[i][0] + acc_r[i + 1][0] + dp2[root][0]
        dp2[child][1] = acc_l[i][1] + acc_r[i + 1][1] + dp2[root][1]
        dp2[child][1] += dp2[child][0]
        dp2[child][0] += 1
        dfs2(child, root)

def iterative_dfs2(root:int):
    stack = [root]
    parent = [-1] * N
    
    while stack:
        cur = stack.pop()
        children = [nei for nei in adj[cur] if nei != parent[cur]]
        acc_l = [[0, 0] for _ in range(len(children) + 1)]
        acc_r = [[0, 0] for _ in range(len(children) + 1)]

        for i in range(len(children)):
            child = children[i]
            acc_l[i + 1][0] = acc_l[i][0] + dp1[child][0]
            acc_l[i + 1][1] = acc_l[i][1] + sum(dp1[child])

        for i in range(len(children) - 1, -1, -1):
            child = children[i]
            acc_r[i][0] = acc_r[i + 1][0] + dp1[child][0]
            acc_r[i][1] = acc_r[i + 1][1] + sum(dp1[child])

        for i, child in enumerate(children):
            dp2[child][0] = acc_l[i][0] + acc_r[i + 1][0] + dp2[cur][0]
            dp2[child][1] = acc_l[i][1] + acc_r[i + 1][1] + dp2[cur][1]
            dp2[child][1] += dp2[child][0]
            dp2[child][0] += 1
            parent[child] = cur
            stack.append(child)

iterative_dfs1(0)
iterative_dfs2(0)
res = []
for i in range(N):
    res.append(dp1[i][1] + dp2[i][1])

print(*res, sep="\n")



# N = int(input())
# adj = [[] for _ in range(N)]

# for _ in range(N - 1):
#     u, v = map(int, input().split())
#     u -= 1
#     v -= 1
#     adj[u].append(v)
#     adj[v].append(u)

# parent = [-1] * N
# depth = [0] * N
# order = []

# stack = [0]

# while stack:
#     v = stack.pop()
#     order.append(v)

#     for child in adj[v]:
#         if child == parent[v]:
#             continue

#         parent[child] = v
#         depth[child] = depth[v] + 1
#         stack.append(child)

# subtree_size = [1] * N

# for v in reversed(order):
#     if parent[v] != -1:
#         subtree_size[parent[v]] += subtree_size[v]

# answer = [0] * N
# answer[0] = sum(depth)

# # 根を順番に移す
# for v in order:
#     for child in adj[v]:
#         if parent[child] != v:
#             continue

#         answer[child] = (
#             answer[v]
#             + N
#             - 2 * subtree_size[child]
#         )

# print(*answer, sep="\n")