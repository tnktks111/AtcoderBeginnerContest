from collections import deque
Q=int(input())
S = deque([1])
cur = 1
digit = 1
MOD = 998244353
i = 0
digit_to_mod = {1:10}
for _ in range(Q):
    query = list(map(int, input().split()))
    if (query[0] == 1):
        S.append(query[1])
        cur = cur * 10 + query[1]
        cur %= MOD
        digit += 1
        if digit not in digit_to_mod:
            digit_to_mod[digit] = (digit_to_mod[digit - 1] * 10) % MOD
    elif (query[0] == 2):
        top = S.popleft()
        digit -= 1
        cur = (cur - top * digit_to_mod[digit]) % MOD
    elif (query[0] == 3):
        print(cur)