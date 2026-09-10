N, M = map(int, input().split())

adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    x -= 1
    seen = set()
    seen.add(x)
    stack = [x]
    for _ in range(k):
        new_stack = []
        for cur in stack:
            for nei in adj[cur]:
                if nei not in seen:
                    seen.add(nei)
                    new_stack.append(nei)
        stack = new_stack
    res = sum(seen) + len(seen)
    print(res)

        