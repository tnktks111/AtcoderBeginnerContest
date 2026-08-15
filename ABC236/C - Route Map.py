N, M = map(int, input().split())
stations = list(input().split())
express = set(input().split())
for i in range(N):
    if stations[i] in express:
        print("Yes")
    else:
        print("No")