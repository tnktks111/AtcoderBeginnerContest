from random import randint

N, Q = 5, 1
print(N, Q)
A = []
for i in range(N):
    A.append(randint(1, 10))
B = []
for i in range(N):
    B.append(randint(1, 10))
print(*A)
print(*B)

for _ in range(Q):
    S = randint(1, N)
    T = randint(S + 1, N + 1)
    print(S, T)