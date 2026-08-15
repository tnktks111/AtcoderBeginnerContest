from collections import defaultdict
N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
color_to_R_and_idx = defaultdict(list)
for i in range(N):
    color_to_R_and_idx[C[i]].append((R[i], i + 1))
if T in color_to_R_and_idx:
    print(max(color_to_R_and_idx[T])[1])
else:
    print(max(color_to_R_and_idx[C[0]])[1])