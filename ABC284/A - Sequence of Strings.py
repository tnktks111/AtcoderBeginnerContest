N = int(input())
names = [input() for _ in range(N)]
print(*names[::-1], sep="\n")