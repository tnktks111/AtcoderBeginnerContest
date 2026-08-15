import sys
sys.setrecursionlimit(10 ** 8)

A = [list(map(int, input().split())) for _ in range(4)]
DIR4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def idx2pos(n:int):
    return tuple(divmod(n, 4))
def pos2idx(r:int, c:int):
    return 4 * r + c

houses = [(r, c) for r in range(4) for c in range(4) if A[r][c] == 1]

def meet_condition(pattern:int, houses:list[tuple[int, int]]):
    for r, c in houses:
        idx = pos2idx(r, c)
        if pattern & (1 << idx) == 0:
            return False

    surrounded = set()
    not_surrounded = set()
    start = None
    for i in range(16):
        if (1 << i) & pattern:
            surrounded.add(i)
            start = i
        else:
            not_surrounded.add(i)

    stack = [start]
    seen = set()
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        r, c = idx2pos(cur)
        for dr, dc in DIR4:
            nr, nc = r + dr, c + dc
            nxt = pos2idx(nr, nc)
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            if nxt in seen:
                continue
            if nxt not in surrounded:
                continue
            stack.append(nxt)

    if len(surrounded) != len(seen):
        return False

    stack = [a for a in not_surrounded if 0 <= a <= 3 or a % 4 == 0 or a % 4 == 3 or 12 <= a <= 15]
    seen = set()
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        r, c = idx2pos(cur)
        for dr, dc in DIR4:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            nxt = pos2idx(nr, nc)
            if nxt in seen:
                continue
            if nxt not in not_surrounded:
                continue
            stack.append(nxt)

    if len(seen) != len(not_surrounded):
        return False

    return True


res = 0
for pattern in range(1 << 16):
    if meet_condition(pattern, houses):
        res += 1
        # print("="*10)
        # print(f"{pattern:016b}"[::-1][:4])
        # print(f"{pattern:016b}"[::-1][4:8])
        # print(f"{pattern:016b}"[::-1][8:12])
        # print(f"{pattern:016b}"[::-1][12:])

print(res)