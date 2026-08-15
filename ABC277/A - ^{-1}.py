N, X = map(int, input().split())
P = list(map(int, input().split()))
num_to_idx = {P[i]:i for i in range(N)}
print(num_to_idx[X] + 1)