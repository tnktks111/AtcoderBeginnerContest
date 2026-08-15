N = int(input())
S = [0] + list(map(int, input().split()))
res = [S[i + 1] - S[i] for i in range(N)]
print(*res)
    