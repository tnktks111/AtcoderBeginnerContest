import heapq
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
target = N

Minstack = []
res = {}
for i in range(N):
    heapq.heappush(Minstack, [T[i], i])

while(target):
	t_idx, idx = heapq.heappop(Minstack)
	if idx not in res:
		res[idx] = t_idx
		target -= 1
	heapq.heappush(Minstack, [t_idx + S[idx], (idx + 1) % N])

for i in range(N):
    print(res[i])