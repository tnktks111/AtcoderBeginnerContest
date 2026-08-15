import math
from collections import deque
def gen_move_vec(d:int) -> list:
    base = []
    res = set()
    sign = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(math.floor(math.sqrt(d)) + 1):
        if math.sqrt(d - i ** 2).is_integer():
            base.append((i, int(math.sqrt(d - i ** 2))))
    base = list(set(base))
    for x, y in base:
        for sign_x, sign_y in sign:
            res.add((x * sign_x, y * sign_y))
    return (list(res))  

N, M = map(int, input().split())
board = [[-1] * N for _ in range(N)]
directions = gen_move_vec(M)
board[0][0] = 0
q = deque([(0, 0)])
seen = set([(0, 0)])
while q:
    # print(q)
    for i in range(len(q)):
        cur_x, cur_y = q.popleft()
        cur_score = board[cur_x][cur_y]
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if not 0 <= next_x < N or not 0 <= next_y < N or (next_x, next_y) in seen:
                continue
            board[next_x][next_y] = cur_score + 1
            seen.add((next_x, next_y))
            q.append((next_x, next_y))
for i in range(N):
    print(*board[i])