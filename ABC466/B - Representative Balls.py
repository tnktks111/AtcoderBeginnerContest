N, M = map(int, input().split())

max_sizes = [-1] * M

for _ in range(N):
    c, s = map(int, input().split())
    c -= 1
    max_sizes[c] = max(s, max_sizes[c])

print(*max_sizes)
