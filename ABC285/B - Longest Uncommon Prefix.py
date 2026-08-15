N = int(input())
S = input()
for i in range(1, N):
    for j in range(0, N - i):
        if S[j] == S[i + j]:
            print(j)
            break
        if j == N - i - 1:
            print(j + 1)