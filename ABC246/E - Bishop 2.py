from collections import deque

from enum import IntEnum

class Direction(IntEnum):
    UP_RIGHT = 0
    DOWN_RIGHT = 1
    DOWN_LEFT = 2
    UP_LEFT = 3

def dir2delta(dir:Direction):
    deltas = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    return deltas[int(dir)]

N = int(input())
INF = float("inf")
DIRECTIONS = [Direction.UP_LEFT, Direction.UP_RIGHT, Direction.DOWN_LEFT, Direction.DOWN_RIGHT]

start = tuple(map(lambda x: int(x) - 1, input().split()))
goal = tuple(map(lambda x: int(x) - 1, input().split()))

S = [input() for _ in range(N)]
dist = [[[INF, INF, INF, INF] for _ in range(N)] for _ in range(N)]

q = deque()
for dir in DIRECTIONS:
    q.append((1, start, dir))
    dist[start[0]][start[1]][int(dir)] = 0

while q:
    d, (r, c), dir = q.popleft()
    if (r, c) == goal:
        break
    for next_dir in DIRECTIONS:
        if next_dir == dir:
            next_d = d
        else:
            next_d = d + 1
        dr, dc = dir2delta(next_dir)
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if S[nr][nc] == "#":
            continue
        if dist[nr][nc][int(next_dir)] <= next_d:
            continue
        dist[nr][nc][int(next_dir)] = next_d
        if next_d == d:
            q.appendleft((next_d, (nr, nc), next_dir))
        else:
            q.append((next_d, (nr, nc), next_dir))

res = min(dist[goal[0]][goal[1]])
if res != INF:
    print(res)
else:
    print(-1)    