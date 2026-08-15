N, A, B = map(int, input().split())

def gcd(a:int, b:int) -> int:
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a:int, b:int) -> int:
    return (a * b // gcd(a, b))

def inc_sum(n: int):
    return (n * (n + 1) // 2)

res = inc_sum(N)
min_unit = lcm(A, B)
unit_sum = A * inc_sum(min_unit // A) + B * inc_sum(min_unit // B) - min_unit
unit_cnt = min_unit // A + min_unit // B - 1

div, mod = N // min_unit, N % min_unit

res -= unit_sum * div
res -= inc_sum(div - 1) * min_unit * unit_cnt

res -= (A * inc_sum(mod // A) + B * inc_sum(mod // B))
res -= (mod // A + mod // B) * min_unit * div

print(res)

# 最初の発想。足し上げていくよりひくほうが効率いいことに気づく
# min_unit = lcm(A, B)
# cnt = 0
# unit_sum = 0
# nums = [True] * min_unit
# for i in range(min_unit // A):
#     nums[A * (i + 1) - 1] = False
# for i in range(min_unit // B):
#     nums[B * (i + 1) - 1] = False
# for i in range(min_unit):
#     if nums[i]:
#         cnt += 1
#         unit_sum += (i + 1)

# div, mod = N // min_unit, N % min_unit

# res = 0
# for i in range(mod):
#     if nums[i]:
#         res += (div * min_unit + i + 1)

# res += div * unit_sum
# res += ((div - 1) * div // 2) * min_unit * cnt

# print(res)