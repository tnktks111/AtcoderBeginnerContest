from collections import deque

def solve():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj[a].append(b)
        adj[b].append(a)

    def bfs(root:int):
        stack = [root]
        parent = [-1] * N
        dists = [-1] * N
        dists[root] = 0

        cur_dist = 1
        while stack:
            new_stack = []
            for cur in stack:
                for nei in adj[cur]:
                    if nei == parent[cur]:
                        continue
                    if dists[nei] == -1:
                        parent[nei] = cur
                        dists[nei] = cur_dist
                        new_stack.append(nei)
                    else:
                        if dists[nei] % 2 == dists[cur] % 2:
                            # print("nei:", nei, "cur:", cur)
                            path_cur = []
                            tmp = cur
                            while tmp != -1:
                                path_cur.append(tmp + 1)
                                tmp = parent[tmp]
                            path_cur = path_cur[::-1]
                            path_nei = []
                            tmp = nei
                            while tmp != -1:
                                path_nei.append(tmp + 1)
                                tmp = parent[tmp]
                            path_nei = path_nei[::-1]
                            start = 0
                            while path_cur[start + 1] == path_nei[start + 1]:
                                start += 1
                            path_cur = path_cur[start:]
                            path_nei = path_nei[start:]
                            return path_cur + path_nei[::-1][:-1]
                        else:
                            continue
            stack = new_stack
            cur_dist += 1

        return []
    res = bfs(0)
    if res:
        print(len(res))
        print(*res)
    else:
        print(-1)

T = int(input())
for _ in range(T):
    solve()

                            

