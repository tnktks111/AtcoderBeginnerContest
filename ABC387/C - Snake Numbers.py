from collections import defaultdict

L, R = map(int, input().split())

def solve(n:int):
    n_str = str(n)
    d = len(n_str)
    
    dp = dict()
    for first in range(int(n_str[0]) + 1):
        dp[(first, (first == int(n_str[0])))] = 1
    
    for nd_char in n_str[1:]:
        next_dp = defaultdict(int)
        nd = int(nd_char)
        for (start, tight), value in dp.items():
            if start == 0:
                for x in range(10):
                    next_dp[(x, False)] += value
            else:
                limit = min(nd, start - 1) if tight else start - 1
                for x in range(limit + 1):
                    next_tight = tight and x == nd
                    next_dp[(start, next_tight)] += value
        dp = next_dp
    
    return sum(dp.values())

print(solve(R) - solve(L - 1))