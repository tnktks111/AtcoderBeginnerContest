import sys
sys.setrecursionlimit(10**6)
S = input()
Q = int(input())

mp = ["BC", "CA", "AB"]
mp2 = ["CAAB", "ABBC", "BCCA"]
memo = {}
def search(t, k, s):
    if (t, k) in memo:
        return memo[(t, k)]
    if t == 0:
        memo[(t, k)] = s[k - 1]
        return s[k - 1]
    if t == 1:
        memo[(t, k)] = mp[ord(s[(k - 1) // 2]) - ord("A")][(k - 1) % 2]
        return memo[(t, k)]
    if k == 1:
        memo[(t, k)] = chr(ord("A") + (ord(S[0]) - ord("A") + t) % 3)
        return memo[(t, k)]
    memo[(t, k)] =  mp2[ord(search(t-2, (k - 1) // 4 + 1, s)) - ord("A")][(k - 1) % 4]
    return memo[(t, k)]
for _ in range(Q):
    T, K = map(int, input().split())
    print(search(T, K, S))
