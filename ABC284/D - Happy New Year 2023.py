import math

def find_pq(n:int) -> tuple[int, int]:
    for i in range(2, math.floor(math.isqrt(n) + 1)):
        if n % i == 0:
            #(p,pq)パターン
            if ((n // i) % i)== 0:
                return (i, n // (i ** 2))
            #(q, p^2)パターン
            else:
                return (int(math.sqrt(n // i)), i)

T = int(input())
for _ in range(T):
    q = int(input())
    print(*find_pq(q))