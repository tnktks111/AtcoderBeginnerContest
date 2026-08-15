N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

mod_sum_list = [[]]
for i in range(1, N + 1):
    tmp = [[0] * i for _ in range(i + 1)]
    tmp[0][0] = 1
    mod_sum_list.append(tmp)

def add_to_mod_sum_list(k:int, i:int, a:int):
    # print(k, i, a, flush=True)
    cur_square = mod_sum_list[k]
    for h in range(min(i, k), 0, -1):
        for w in range(k):
            cur_square[h][w] += cur_square[h - 1][(w - a) % k]
            cur_square[h][w] %= MOD
    # print(mod_sum_list)
for i in range(1, N + 1):
    a = A[i - 1]
    for j in range(1, N + 1):
        add_to_mod_sum_list(j, i, a)

res = 0
for i in range(1, N + 1):
    cur_square = mod_sum_list[i]
    res += cur_square[i][0]
    res %= MOD
print(res)