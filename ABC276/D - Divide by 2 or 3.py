N = int(input())
A = list(map(int, input().split()))

def gcd(a:int, b:int):
    if a > b:
        return gcd(b, a)
    if b % a == 0:
        return a
    return gcd(a, b % a)

def can_divide_only_by_two_three(n:int):
    cnt = 0
    while not n & 1:
        n >>= 1
        cnt += 1
    while n % 3 == 0:
        n //= 3
        cnt += 1
    return (n == 1, cnt)
    
A_gcd = A[0]
for i in range(1, len(A)):
    A_gcd = gcd(A_gcd, A[i])
for i in range(len(A)):
    A[i] //= A_gcd

res = 0
for i in range(len(A)):
    ok, cnt = can_divide_only_by_two_three(A[i])
    if not ok:
        print(-1)
        exit()
    res += cnt

print(res)

        
    