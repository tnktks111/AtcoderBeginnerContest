import itertools, math
from collections import defaultdict
N, M = map(int, input().split())
S = list(input() for _ in range(N))
S_to_int = {S[i]:i for i in range(N)}
SumS = sum([len(S[i]) for i in range(N)])
T = list(input() for _ in range(M))
T_set = set()
T_to_sep_cnt = defaultdict(set)

def combination(n:int, k:int):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def combination_sum(len:int, s:int):
    res = []
    def dfs(i:int, len:int, cur:list, rest:int):
        if i == len:
            res.append(tuple(cur))
            return 
        for j in range(1, max(rest - (len - 1 - i) + 1, 1)):
            cur.append(j)
            dfs(i + 1, len, cur, rest - j)
            cur.pop()
    dfs(0, len, [], s)
    return res

if N == 1 and len(S[0]) < 3:
    print(-1)
    exit()

for i in range(M):
    tmp = []
    streaks = []
    seen = set()
    fail = False
    T_split = T[i].split("_")
    if T_split[0] == "" or T_split[-1] == "":
        continue
    streak = 0
    # print(T_split)
    for i in range(len(T_split)):
        if T_split[i] == "":
            streak += 1
        else:
            if T_split[i] not in S or T_split[i] in seen:
                fail = True
                break
            seen.add(T_split[i])
            if streak > 0:
                streaks.append(streak)
            streak = 1
            tmp.append(S_to_int[T_split[i]])
    if fail or len(tmp) != N:
        continue
    T_set.add(tuple(tmp))
    T_to_sep_cnt[tuple(tmp)].add(tuple(streaks))

margins = set(combination_sum(N - 1, 16 - SumS))

# print(T_to_sep_cnt)
# print(margins)

possibles = list(itertools.permutations(tuple([i for i in range(N)])))
res = []
for possible in possibles:
    if possible not in T_set:
        for i in possible:
            res.append(S[i])
        print(*res, sep="_")
        exit()
    else:
        if margins - T_to_sep_cnt[possible]:
            margin = list(margins - T_to_sep_cnt[possible])[0]
            res = []
            for i in range(len(possible)):
                res.append(S[possible[i]])
                if i != len(possible) - 1:
                    res.append("_" * margin[i])
            print("".join(res))
            exit()
print(-1)