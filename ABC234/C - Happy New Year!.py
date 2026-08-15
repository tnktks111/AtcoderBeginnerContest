from collections import deque
K = int(input())
Q = deque()
digits = {1:"2", 0:"0"}
while K:
    Q.appendleft(digits[K % 2])
    K //= 2
print("".join(Q))
