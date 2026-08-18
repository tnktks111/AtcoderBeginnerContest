N, Q = map(int, input().split())
X = list(map(int, input().split()))

def merge_20(subtree_ranks:list[list[int]]):
    merged_list = []
    for l in subtree_ranks:
        merged_list.extend(l)
    merged_list.sort(reverse=True)
    return merged_list[:20]

adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

ranks = [[] for _ in range(N)]

def iterative_dfs(root:int):
    stack = [root]
    parents = [-1] * N
    seen = set()
    while stack:
        cur = stack.pop()
        if cur not in seen:
            stack.append(cur)
            seen.add(cur)
            for nei in adj[cur]:
                if nei == parents[cur]:
                    continue
                parents[nei] = cur
                stack.append(nei)
        else:
            subtree_ranks = [[X[cur]] + [0] * 19]
            for nei in adj[cur]:
                if nei == parents[cur]:
                    continue
                subtree_ranks.append(ranks[nei])
            ranks[cur] = merge_20(subtree_ranks)

iterative_dfs(0)

for _ in range(Q):
    v, k = map(lambda x: int(x) - 1, input().split())
    print(ranks[v][k])
