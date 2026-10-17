N, M = map(int, input().split())

costs = []
roulettes = []

for _ in range(N):
    c, p, *roulette = map(int, input().split())
    costs.append(c)
    roulettes.append(roulette)

dp = [0] * (M + 1)

for i in range(1, M + 1):
    candidates = []
    for j in range(N):
        candidate = costs[j]
        dont_move_cnt = 0
        for k in range(len(roulettes[j])):
            if roulettes[j][k] == 0:
                dont_move_cnt += 1
            elif i - roulettes[j][k] >= 0:
                candidate += (dp[i - roulettes[j][k]]) / len(roulettes[j])
        candidate /= (1 - dont_move_cnt / len(roulettes[j]))
        candidates.append(candidate)
    # print(candidates)
    dp[i] = min(candidates)

# print(dp)
print(dp[-1])