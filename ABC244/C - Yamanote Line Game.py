from collections import deque
N = int(input())
remain = set(list(range(2 * N + 1))) #0-indexed
pool = deque(list(range(2 * N + 1))) #0-indexed
list(range(2 * N + 1))
for _ in range(N + 1):
    cur = pool.popleft()
    while cur not in remain:
        cur = pool.popleft()
    print(cur + 1, flush=True)
    remain.remove(int(input()) - 1)
    