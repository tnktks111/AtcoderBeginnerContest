L, R = map(int, input().split())
S = list(input())
L, R = L - 1, R - 1
while L < R:
    S[L], S[R] = S[R], S[L]
    L, R = L + 1, R - 1
print("".join(S))