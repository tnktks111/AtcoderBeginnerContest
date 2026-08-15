from collections import defaultdict
N, X = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 5
hashmap = defaultdict(list)

for i in range(N):
    pair1 = A[i] + X
    pair2 = A[i] - X
    hashkey = A[i] % MOD
    hashmap[hashkey].append(A[i])
    candidates = hashmap.get(pair1 % MOD, [])
    if pair1 in candidates:
        print("Yes")
        exit()
    candidates = hashmap.get(pair2 % MOD, [])
    if pair2 in candidates:
        print("Yes")
        exit()
print("No")