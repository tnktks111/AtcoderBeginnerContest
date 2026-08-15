N = int(input())
A = [0] + list(map(int, input().split()))

num_idx_same_pair_cnt = 0
good_pair = 0
for i in range(1, N + 1):
    if i == A[i]:
        num_idx_same_pair_cnt += 1
    elif 0 < A[i] < N + 1 and i == A[A[i]]:
        good_pair += 1
     

print(num_idx_same_pair_cnt * (num_idx_same_pair_cnt - 1) // 2 + good_pair // 2)
