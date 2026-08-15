MOD = 998244353
N = int(input())

prev = [1, 1]
cur = [0, 0]
prev_A, prev_B = map(int, input().split())

for i in range(1, N):
    curr_A, curr_B = map(int, input().split())
    if curr_A != prev_A:
        cur[0] += prev[0]
    if curr_A != prev_B:
        cur[0] += prev[1]
    if curr_B != prev_A:
        cur[1] += prev[0]
    if curr_B != prev_B:
        cur[1] += prev[1]
    cur[0] %= MOD
    cur[1] %= MOD
    if (cur[0] == 0 and cur[1] == 0):
        print(0)
        exit()
    prev[0], prev[1] = cur[0], cur[1]
    prev_A, prev_B = curr_A, curr_B
    cur = [0, 0]

print(sum(prev) % MOD)