N = int(input())
X = sorted(list(map(int, input().split())))
print(sum(X[N:-N]) / (len(X) - 2 * N))