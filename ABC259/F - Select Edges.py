import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
D = list(map(int, input().split()))

adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

def dfs(root:int, parent:int):
    use_parent = 0
    not_use_parent = 0

    use_children_edge = []
    separate_children_edge = []
    differences = []

    if parent != -1 and len(adj[root]) <= 1:
        return 0, 0

    for nei, weight in adj[root]:
        if nei == parent:
            continue
        u, n = dfs(nei, root)
        if D[nei] > 0:
            use_children_edge.append(u + weight)
        else:
            use_children_edge.append(u)
        separate_children_edge.append(n)
        differences.append(use_children_edge[-1] - separate_children_edge[-1])
    sorted_differences = sorted(differences, reverse=True)
    # print("sorted: ", sorted_differences)

    d = D[root]
    use_parent, not_use_parent = sum(separate_children_edge), sum(separate_children_edge)
    
    if d > 1:
        for i in range(min(d - 1, len(sorted_differences))):
            if sorted_differences[i] < 0:
                break
            use_parent += sorted_differences[i]
    
    if d > 0:
        for i in range(min(d, len(sorted_differences))):
            if sorted_differences[i] < 0:
                break
            not_use_parent += sorted_differences[i]


    return use_parent, not_use_parent

print(max(dfs(0, -1)))