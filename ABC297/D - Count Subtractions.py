A, B = map(int, input().split())
cnt = 0

while A != B:
    if A < B:
        A, B = B, A
    q, mod = divmod(A, B)
    if mod == 0:
        q -= 1
        mod = B
    cnt += q
    A = mod

print(cnt)