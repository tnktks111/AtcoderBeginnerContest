from collections import deque
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for a, b in AB:
    Q.append(a / b)
res = 0
cur_idx = 0
while (len(Q) > 1):
    left = Q.popleft()
    right = Q.pop()
    if left > right:
        res += right * AB[cur_idx][1]
        Q.appendleft(left - right)
    else:
        res += left * AB[cur_idx][1]
        Q.append(right - left)
        cur_idx += 1
if Q:
    res += (Q.pop() / 2) * AB[cur_idx][1]
print(res)