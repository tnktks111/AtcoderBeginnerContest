N = int(input())
arrays = set()
for _ in range(N):
    arrays.add(tuple(map(int, input().split())))
print(len(arrays))