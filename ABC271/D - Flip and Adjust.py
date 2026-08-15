from collections import deque
N, S = map(int, input().split())

q = deque([(0, "")])
for _ in range(N):
    a, b = map(int, input().split())
    seen = set()
    for _ in range(len(q)):
        i, s = q.popleft()
        if i + a <= S and i + a not in seen:
            q.append((i + a, s+"H"))
            seen.add(i + a)
        if i + b <= S and i + b not in seen:
            q.append((i + b, s+"T"))
            seen.add(i + b)
final = sorted(list(set(q)), reverse=True)
print(f"Yes\n{final[0][1]}" if final[0][0] == S else "No")
