from functools import cache
N = int(input())

children = [[] for _ in range(N)]

for i in range(1, N):
    boss = int(input()) - 1
    children[boss].append(i)

@cache
def dfs(i:int):
    if len(children[i]) == 0:
        return 1
    minimim = float("inf")
    maximum = -1
    for child in children[i]:
        child_salary = dfs(child)
        minimim = min(minimim, child_salary)
        maximum = max(maximum, child_salary)
    return 1 + minimim + maximum

print(dfs(0))