N = int(input())
S = input()
MOD = 998244353

char_set = list(set(S))
# print(char_set)
n_char = len(char_set)
char2idx = {c: i for i, c in enumerate(char_set)}

dp = [[0] * (1 + n_char) for _ in range(1 << n_char)]
dp[0][0] = 1

for c in S:
    nxt_char = char2idx[c]
    next_dp = [[0] * (1 + n_char) for _ in range(1 << n_char)]
    for prv_history in range(1 << n_char):
        if prv_history == 0:
            next_dp[0][0] = 1
            next_dp[(1 << nxt_char)][1 + nxt_char] += 1
            next_dp[(1 << nxt_char)][1 + nxt_char] %= MOD
        else:
            for prv_char in range(n_char):
                # 使わない場合
                next_dp[prv_history][1 + prv_char] += dp[prv_history][1 + prv_char]
                next_dp[prv_history][1 + prv_char] %= MOD
                if (1 << prv_char) & prv_history == 0:
                    continue
                # 使う場合(同じ文字の連続か、新規の文字)
                if prv_char == nxt_char:
                    next_dp[prv_history][1 + nxt_char] += dp[prv_history][1 + prv_char]
                    next_dp[prv_history][1 + nxt_char] %= MOD
                elif (1 << nxt_char) & prv_history == 0:
                    nxt_history = (1 << nxt_char) | prv_history
                    next_dp[nxt_history][1 + nxt_char] += dp[prv_history][1 + prv_char]
                    next_dp[nxt_history][1 + nxt_char] %= MOD
    dp = next_dp
    # print("=" * 20)
    # print(*dp, sep="\n")

res = 0
for r in range(1 << n_char):
    if r == 0:
        continue
    for c in range(1, 1 + n_char):
        res += dp[r][c]
        res %= MOD
print(res)