N, X = map(int, input().split())
coins = {}
bitset = 1
mask = 2 ** (X + 1) - 1
for _ in range(N):
    yen, cnt = map(int, input().split())
    for i in range(1, cnt + 1):
        bitset |= ((bitset << yen) & mask)
    # print(bin(bitset))
print("Yes" if (bitset >> X) else "No")
