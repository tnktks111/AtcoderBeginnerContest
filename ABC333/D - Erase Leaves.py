import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)

def delete_subtree(root:int, parent:int):
    res = 1
    for nei in adj[root]:
        if nei == parent:
            continue
        res += delete_subtree(nei, root)
    return res

delete_subtree_cnt = []
for nei in adj[0]:
    delete_subtree_cnt.append(delete_subtree(nei, 0))
print(sum(delete_subtree_cnt) - max(delete_subtree_cnt) + 1)