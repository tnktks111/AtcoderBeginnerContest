INF = float("inf")
N, Q = map(int, input().split())
L = [INF] + list(map(int, input().split()))
R = list(map(int, input().split())) + [INF]

left_min = [INF] * N
right_min = [INF] * N

for i in range(1, N):
    right_min[i] = min(right_min[i - 1], R[i - 1])

for i in range(N - 2, -1, -1):
    left_min[i] = min(left_min[i + 1], L[i + 1])

for _ in range(Q):
    s, t = map(lambda x: int(x) - 1, input().split())
    if s < t:
        print(min(R[s], L[s] + right_min[s]))
    else:
        print(min(L[s], R[s] + left_min[s]))
