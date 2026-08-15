class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + int(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod
T = int(input())

MOD = 2 ** 61 - 1
BASE = 3

for _ in range(T):
    A, B = input(), input()
    A = A + A
    ra = RollingHash(A, 3, MOD)
    rb = RollingHash(B, 3, MOD)
    target = rb.get(0, len(B))
    ok = False
    for i in range(len(A) - len(B) + 1):
        if target == ra.get(i, i + len(B)):
            print(i)
            ok = True
            break
    if not ok:
        print(-1)
