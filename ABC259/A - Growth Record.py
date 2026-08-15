N, M, X, T, D = map(int, input().split())
print(T - X * D + min(M, X) * D)