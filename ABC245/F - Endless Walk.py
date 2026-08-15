import sys
import typing

sys.setrecursionlimit(2 * 10 ** 5)

class CSR:
    def __init__(
            self, n: int, edges: typing.List[typing.Tuple[int, int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)

        for e in edges:
            self.start[e[0] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = self.start.copy()
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1


class SCCGraph:
    '''
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    '''

    def __init__(self, n: int) -> None:
        self._n = n
        self._edges: typing.List[typing.Tuple[int, int]] = []

    def num_vertices(self) -> int:
        return self._n

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self._edges.append((from_vertex, to_vertex))

    def scc_ids(self) -> typing.Tuple[int, typing.List[int]]:
        g = CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def scc(self) -> typing.List[typing.List[int]]:
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: typing.List[typing.List[int]] = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups
    
    
    def condensation_graph(
        self,
    ) -> typing.Tuple[
        typing.List[typing.List[int]],  # 各SCCに属する頂点
        typing.List[typing.List[int]],  # 縮約DAGの隣接リスト
        typing.List[int],               # 各SCCの入次数
        typing.List[int],               # 各頂点のSCC番号
    ]:
        group_num, ids = self.scc_ids()

        groups: typing.List[typing.List[int]] = [
            [] for _ in range(group_num)
        ]

        for v in range(self._n):
            groups[ids[v]].append(v)

        dag_set: typing.List[typing.Set[int]] = [
            set() for _ in range(group_num)
        ]

        for u, v in self._edges:
            component_u = ids[u]
            component_v = ids[v]

            if component_u != component_v:
                dag_set[component_u].add(component_v)

        dag = [list(neighbors) for neighbors in dag_set]

        indegree = [0] * group_num

        for component_u in range(group_num):
            for component_v in dag[component_u]:
                indegree[component_v] += 1

        return groups, dag, indegree, ids

N, M = map(int, input().split())
graph = SCCGraph(N)

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph.add_edge(a, b)

groups, dag, indegree, component_id = graph.condensation_graph()

# 強連結成分iが要素数2以上の強連結成分へ到達可能かどうか
# -1:未定, 0:不可, 1:可能
dp = [-1] * len(dag)
def dfs(id:int):
    if dp[id] != -1:
        return dp[id]
    if len(groups[id]) > 1:
        dp[id] = 1
        return dp[id]
    for nei in dag[id]:
        if dfs(nei) == 1:
            dp[id] = 1
            return 1
    dp[id] = 0
    return 0

res = 0
for id in range(len(dag)):
    if dfs(id) == 1:
        res += len(groups[id])
print(res)