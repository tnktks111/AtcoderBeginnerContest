from collections import deque
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A_even = [A[i] for i in range(N) if (i & 1) ^ 1]
A_odd = [A[i] for i in range(N) if i & 1]

q = deque([A[0]])
for i in range(1, len(A_even)):
    seen = set()
    for j in range(len(q)):
        pre = q.popleft()
        if abs(pre + A_even[i]) <= 10 ** 4 and pre + A_even[i] not in seen:
            q.append(pre + A_even[i])
            seen.add(pre + A_even[i])
        if abs(pre - A_even[i]) <= 10 ** 4 and pre - A_even[i] not in seen:
            q.append(pre - A_even[i])
            seen.add(pre - A_even[i])
if X not in set(q):
    print("No")
    exit()

q = deque([0])
for i in range(len(A_odd)):
    seen = set()
    for j in range(len(q)):
        pre = q.popleft()
        if abs(pre + A_odd[i]) <= 10 ** 4 and pre + A_odd[i] not in seen:
            q.append(pre + A_odd[i])
            seen.add(pre + A_odd[i])
        if abs(pre - A_odd[i]) <= 10 ** 4 and pre - A_odd[i] not in seen:
            q.append(pre - A_odd[i])
            seen.add(pre - A_odd[i])
if Y not in set(q):
    print("No")
    exit()

print("Yes")