N = int(input())
k = -1
while N:
    N //= 2
    k += 1
print(k)