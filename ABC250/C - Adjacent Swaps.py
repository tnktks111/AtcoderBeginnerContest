N, Q = map(int, input().split())
n_to_idx = [i for i in range(N)]
idx_to_n = [i for i in range(N)]
for _ in range(Q):
    x = int(input()) - 1
    x_idx = n_to_idx[x]
    y = idx_to_n[x_idx + 1] if x_idx != N - 1 else idx_to_n[N - 2]
    y_idx = n_to_idx[y]
    n_to_idx[x], idx_to_n[x_idx], n_to_idx[y], idx_to_n[y_idx] = y_idx, y, x_idx, x
res = map(lambda x: x+1, idx_to_n)
print(*res)