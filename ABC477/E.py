import heapq
from itertools import accumulate

N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = float("inf")

# 中心を1回通る場合
center2dist = [INF] * N
minq = [(B[i], i) for i in range(len(B))]
heapq.heapify(minq)

while minq:
    d, cur = heapq.heappop(minq)
    # print(d, cur)
    if center2dist[cur] <= d:
        continue
    center2dist[cur] = d

    nxt_1 = (cur + 1) % N
    d_1 = d + A[cur]

    if center2dist[nxt_1] > d_1:
        heapq.heappush(minq, (d_1, nxt_1))

    nxt_2 = (cur - 1) % N
    d_2 = d + A[nxt_2]
    if center2dist[nxt_2] > d_2:
        heapq.heappush(minq, (d_2, nxt_2))

# 中心を通らない場合
A_acc = [0] + list(accumulate(A))
# print(center2dist)

for _ in range(Q):
    u, v = map(lambda x: int(x) - 1, input().split())
    res = INF
    if v == N:
        res = center2dist[u]
    else:
        not_use_center_dist_1 = A_acc[v] - A_acc[u]
        not_use_center_dist_2 = A_acc[-1] - not_use_center_dist_1
        # print(not_use_center_dist_1, not_use_center_dist_2, A_acc[-1])
        res = min(not_use_center_dist_1, not_use_center_dist_2, center2dist[u] + center2dist[v])
    print(res)