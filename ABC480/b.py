from collections import defaultdict

INF = float("inf")
N, M = map(int, input().split())

candidates = [input() for _ in range(N)]

candidates_set = set(candidates)

cnts = defaultdict(int)

def diff(s:str, t:str):
    if len(s) != len(t):
        return INF
    res = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            res += 1
    return res

for _ in range(M):
    T = input()
    if T in candidates_set:
        cnts[T] += 1
    else:
        target = None
        invalid = False
        for candidate in candidates:
            if diff(T, candidate) == 1:
                if target is not None:
                    invalid = True
                else:
                    target = candidate
        if not invalid and target is not None:
            cnts[target] += 1

for i in range(N):
    # print(candidates[i])
    print(cnts[candidates[i]])
