from collections import deque
from sortedcontainers import SortedList

N, M = map(int, input().split())

chocorates = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
boxes = list(zip(list(map(int, input().split())), list(map(int, input().split()))))

chocorates.sort()
boxes.sort()

q = deque(chocorates)
waiting_q = SortedList()

for (c, d) in boxes:
    while q and q[0][0] <= c:
        a, b = q.popleft()
        waiting_q.add(b)
    if waiting_q:
        i = waiting_q.bisect_right(d)
        if i == 0:
            continue
        waiting_q.pop(i - 1)
print("Yes" if (not q and not waiting_q) else "No")