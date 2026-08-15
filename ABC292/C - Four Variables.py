import math
N = int(input())
divisors = [0] * N

def cnt_divisor(n:int) -> int:
    res = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            res += 1
    res *= 2
    if (math.sqrt(n)).is_integer():
        res += 1
    return (res)

for i in range(1, N + 1):
    divisors[i - 1] = cnt_divisor(i)

res = 0
for i in range(1, N):
    res += divisors[i - 1] * divisors[N - i - 1]

print(res)