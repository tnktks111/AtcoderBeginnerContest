N = int(input())
P = list(map(int, input().split()))

num2idx = [0] * N
for i, p in enumerate(P):
    num2idx[p] = i

cnts = [0, 0, 0] # +1, 0, -1
events = [[] for _ in range(N)]
diff = 0
for i in range(N):
    if N % 2 == 1:
        half = N // 2
        increase_stop = (i + half - num2idx[i]) % N
        decrease_start = (i - half - num2idx[i]) % N
        increase_start = (i - num2idx[i]) % N
        if increase_stop < decrease_start and increase_stop < increase_start:
            cnts[0] += 1
        elif decrease_start < increase_stop and decrease_start < increase_start:
            cnts[1] += 1
        else:
            cnts[2] += 1
        events[increase_stop].append(0)
        events[decrease_start].append(-1)
        events[increase_start].append(1)
    else:
        half = N // 2
        increase_start = (i - num2idx[i]) % N
        decrease_start = (i + half - num2idx[i]) % N
        if decrease_start < increase_start:
            cnts[0] += 1
        else:
            cnts[2] += 1
        events[decrease_start].append(-1)
        events[increase_start].append(1)

# print(events)
# print(cnts)
res = float("inf")
tmp = 0
for i in range(N):
    tmp += min((num2idx[i] - i) % N, (i - num2idx[i]) % N)

for i in range(N):
    if i != 0:
        tmp += (cnts[0] - cnts[2])
    for event in events[i]:
        if event == 1:
            cnts[2] -= 1
            cnts[0] += 1
        elif event == 0:
            cnts[0] -= 1
            cnts[1] += 1
        else:
            if N % 2 == 1:
                cnts[1] -= 1
                cnts[2] += 1
            else:
                cnts[0] -= 1
                cnts[2] += 1
    # print(tmp)
    res = min(res, tmp)

print(res)