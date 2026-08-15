N, Q = map(int, input().split())
S = input()
start = 0
for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        start = (N + start - (x % N)) % N
    else:
        print(S[(start + x - 1) % N])