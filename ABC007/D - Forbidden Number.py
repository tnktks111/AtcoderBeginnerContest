from collections import defaultdict

A, B = map(int, input().split())

# n以下で4も9も使われている
def solve(n:int):
    str_n = str(n)
    
    dp = {True:1, False:0}
    for nd_char in str_n:
        nd = int(nd_char)
        next_dp = defaultdict(int)

        if nd != 4 and nd != 9:
            next_dp[True] += dp[True]
        
        # nd未満かつ4でも9でもない
        if nd <= 4:
            next_dp[False] += dp[True] * nd
        else:
            next_dp[False] += dp[True] * (nd - 1)

        next_dp[False] += dp[False] * 8

        dp = next_dp
        # print(dp)
    return n - sum(dp.values())

print(solve(B) - solve(A - 1))