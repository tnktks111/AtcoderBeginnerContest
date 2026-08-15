import math

a, b, d = map(int, input().split())
r = math.sqrt(a ** 2 + b ** 2)
theta = math.radians(d)
if a != 0:
    alpha = math.atan2(b, a)
elif b > 0:
    alpha = math.pi / 2
else:
    alpha = (math.pi / 2) * 3 
res = [0, 0]
res[0] = r * math.cos(theta + alpha)
res[1] = r * math.sin(theta + alpha)
print(*res)
