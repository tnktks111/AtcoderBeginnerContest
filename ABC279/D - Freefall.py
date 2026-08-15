import math

A, B = map(int, input().split())

def min_time(A:int, B:int, n:int) -> float:
    return A / math.sqrt(1 + n) + B * n

n = pow(2 * B / A, -2 / 3) - 1
if n < 0:
    print(min_time(A, B, 0))
else:
    print(min(min_time(A, B, math.floor(n)), min_time(A, B, math.ceil(n))))