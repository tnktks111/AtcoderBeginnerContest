from sortedcontainers import SortedList

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

t2idx = {t: i for i, t in enumerate(T)}
T.sort(reverse=True)

res = 0
seen_starts_right = SortedList()
seen_goals_right = SortedList()
seen_starts_left = SortedList()
seen_goals_left = SortedList()


for t in T:
    i = t2idx[t]
    res += abs(S[i] - t)
    if S[i] < t:
        res += seen_starts_right.bisect_left(S[i])
        seen_starts_right.add(S[i])
        seen_goals_right.add(t)
    else:
        res -= seen_starts_right.bisect_left(S[i] + 1)
        res += seen_starts_left.bisect_left(S[i])
        seen_starts_left.add(S[i])
        seen_goals_left.add(t)
    # print("res", res)
print(res)