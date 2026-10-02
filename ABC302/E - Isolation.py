N, Q = map(int, input().split())

adj: list[set[int]] = [set() for _ in range(N)]
n_isolated = N

for _ in range(Q):
    query = tuple(map(int, input().split()))
    # print(*adj, sep="\n")
    # print()
    if query[0] == 1:
        u, v = query[1] - 1, query[2] - 1
        if not adj[u]:
            n_isolated -= 1
        if not adj[v]:
            n_isolated -= 1
        adj[u].add(v)
        adj[v].add(u)
    else:
        v = query[1] - 1
        if adj[v]:
            n_isolated += 1
            for nei in adj[v]:
                adj[nei].remove(v)
                if not adj[nei]:
                    n_isolated += 1
            adj[v] = set()
    print(n_isolated)