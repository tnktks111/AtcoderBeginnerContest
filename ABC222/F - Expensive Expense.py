N = int(input())

adj = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((b, c))
    adj[b].append((a, c))

D = list(map(int, input().split()))

dp_1 = [[-1, -1] for i in range(N)]
dp_1_self_include = [[D[i], i] for i in range(N)] # 親が子を見るとき用

def iterative_dfs1(root:int):
    stack = [root]
    parent = [-1] * N
    seen = [False] * N

    while stack:
        cur = stack.pop()
        if seen[cur]:
            for nei, w in adj[cur]:
                if nei == parent[cur]:
                    continue
                if w + dp_1_self_include[nei][0] >= dp_1[cur][0]:
                    dp_1[cur][0] = w + dp_1_self_include[nei][0]
                    dp_1[cur][1] = dp_1_self_include[nei][1]
            if dp_1[cur][0] > dp_1_self_include[cur][0]:
                dp_1_self_include[cur][0] = dp_1[cur][0]
                dp_1_self_include[cur][1] = dp_1[cur][1]
        else:
            seen[cur] = True
            stack.append(cur)
            for nei, _ in adj[cur]:
                if nei == parent[cur]:
                    continue
                parent[nei] = cur
                stack.append(nei)

# test
# p = 0
# iterative_dfs1(p)
# print(dp_1[p])

iterative_dfs1(0)

dp_2 = [[-1, -1] for i in range(N)]
dp_2_self_include = [[D[i], i] for i in range(N)]
def iterative_dfs2(root:int):
    stack = [root]
    parent = [-1] * N

    while stack:
        cur = stack.pop()
        children = [(nei, w) for nei, w in adj[cur] if nei != parent[cur]]
        
        acc_l = [[-1, -1] for _ in range(len(children) + 1)]
        acc_r = [[-1, -1] for _ in range(len(children) + 1)]
        
        for i in range(len(children)):
            child, w = children[i]
            acc_l[i + 1][0] = acc_l[i][0]
            acc_l[i + 1][1] = acc_l[i][1]
            
            if acc_l[i + 1][0] <= dp_1_self_include[child][0] + w:
                acc_l[i + 1][0] = dp_1_self_include[child][0] + w
                acc_l[i + 1][1] = dp_1_self_include[child][1]
            
        for i in range(len(children) - 1, -1, -1):
            child, w = children[i]
            acc_r[i][0] = acc_r[i + 1][0]
            acc_r[i][1] = acc_r[i + 1][1]
            
            if acc_r[i][0] <= dp_1_self_include[child][0] + w:
                acc_r[i][0] = dp_1_self_include[child][0] + w
                acc_r[i][1] = dp_1_self_include[child][1]
    
        for i, (child, w) in enumerate(children):
            if acc_l[i][0] > acc_r[i + 1][0]:
                dp_2[child][0] = acc_l[i][0]
                dp_2[child][1] = acc_l[i][1]
            else:
                dp_2[child][0] = acc_r[i + 1][0]
                dp_2[child][1] = acc_r[i + 1][1]
            
            if dp_2_self_include[cur][0] > dp_2[child][0]:
                dp_2[child][0] = dp_2_self_include[cur][0]
                dp_2[child][1] = dp_2_self_include[cur][1]
            
            dp_2[child][0] += w

            if dp_2[child][0] > dp_2_self_include[child][0]:
                dp_2_self_include[child][0] = dp_2[child][0]
                dp_2_self_include[child][1] = dp_2[child][1]
            
            parent[child] = cur
            stack.append(child)

iterative_dfs2(0)

ans = [0] * N
for i in range(N):
    ans[i] = max(dp_1[i][0], dp_2[i][0])

print(*ans, sep="\n")