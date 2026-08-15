H, W, N = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
a, b = [list(t) for t in zip(*ab)]
set_a = sorted(set(a))
set_b = sorted(set(b))
dict_a = {set_a[i] : i for i in range(len(set_a))}
dict_b = {set_b[i] : i for i in range(len(set_b))}
for i in range(N):
    s = a[i] - ((a[i] - 1) - dict_a[a[i]])
    t = b[i] - ((b[i] - 1) - dict_b[b[i]])
    print(s, t)
