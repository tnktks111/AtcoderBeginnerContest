import heapq
N, W = map(int, input().split())
AB = [[-a, b] for a, b in [list(map(int, input().split())) for _ in range(N)]]
heapq.heapify(AB)
cur_remain = W
cur_score = 0
while True:
    a, b = heapq.heappop(AB)
    a *= -1
    cur_score += a * min(cur_remain, b)
    if cur_remain < b or not AB:
        break
    cur_remain -= b
print(cur_score)