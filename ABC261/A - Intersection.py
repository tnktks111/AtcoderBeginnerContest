L1, R1, L2, R2 = map(int, input().split())

start = max(L1, L2)
end = min(R1, R2)

if start > end:
    print(0)
else:
    print(end - start)