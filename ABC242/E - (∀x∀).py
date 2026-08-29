T = int(input())
MOD = 998244353

def solve(N:int, S:str):
    # tight, not tight
    dp = 0
    tight_meets_dict_order = True
    for i in range((N + 1) // 2):
        dp = dp * 26 + 1 * (ord(S[i]) - ord("A"))
        dp %= MOD
        if S[i] > S[N - 1 - i]:
            tight_meets_dict_order = False
        elif S[i] < S[N - 1 - i]:
            tight_meets_dict_order = True

    # print(tight_meets_dict_order)
    if tight_meets_dict_order:
        dp = (dp + 1) % MOD
    return dp

for _ in range(T):
    N = int(input())
    S = input()
    print(solve(N, S))