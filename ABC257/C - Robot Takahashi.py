N = int(input())
S = input()
W = list(map(int, input().split()))
num_to_idx = {}
W_sort = sorted(list(set(W)))
for i in range(len(W_sort)):
    num_to_idx[W_sort[i]] = i
DP = [[0] * len(W_sort) for _ in range(2)]
num_child_adalt = [0, 0]
for i in range(N):
    if S[i] == "0":
        DP[0][num_to_idx[W[i]]] += 1
        num_child_adalt[0] += 1
    else:
        DP[1][num_to_idx[W[i]]] += 1
        num_child_adalt[1] += 1

cur = [0, num_child_adalt[1]]
res = num_child_adalt[1]
for i in range(len(W_sort)):
    cur[0] += DP[0][i]
    cur[1] -= DP[1][i]
    res = max(res, cur[0] + cur[1])
print(res)