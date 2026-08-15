from collections import deque, defaultdict

N = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
for i in range(N):
    cnt[A[i]] += 1
sell_cnt = 0
for key, val in cnt.items():
    sell_cnt += (val - 1)
A = list(set(A))
A.sort()
q = deque(A)
prev = 0
while True:
    # print(q)
    if q:
        cur = q.popleft()
        if cur == prev + 1:
            prev += 1
        else:
            q.appendleft(cur)
            if sell_cnt >= 2:
                sell_cnt -= 2
                prev += 1
            elif sell_cnt == 1:
                if not q:
                    break
                sell_cnt -= 1
                q.pop()
                prev += 1
            else:
                if len(q) < 2:
                    break
                q.pop()
                q.pop()
                prev += 1
    else:
        if sell_cnt >= 2:
            prev += 1
            sell_cnt -= 2
        else:
            break
print(prev)