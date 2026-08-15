N, K, A = map(int, input().split())
num = (A + K - 1) % N
if num != 0:
    print(num)
else:
    print(N)