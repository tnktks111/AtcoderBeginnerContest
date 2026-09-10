import math

N = int(input())
nums = []

for i in range(N):
    m = int(input())
    x = 1
    for _ in range(m):
        p, e = map(int, input().split())
        x *= pow(p, e)
    nums.append(x)

lcms = set()
for i in range(N):
    targets = nums[:i] + nums[i+1:]
    lcms.add(math.lcm(*targets))
    
print(len(lcms))