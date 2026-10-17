from random import randint

T = 1
print(T)
for _ in range(T):
    N = randint(1, 10 ** 18)
    X = randint(1, N)
    K = randint(0, N - 1)
    print(N, X, K)
