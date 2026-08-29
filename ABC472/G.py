from copy import deepcopy
H, W = map(int, input().split())

board_auth = [input() for _ in range(H)]
board_copy = [list(board_auth[i]) for i in range(H)]

def clear(r:int, c:int):
    change = set()
    i = c - 1
    while i >= 0 and board_copy[r][i] != "#":
        board_copy[r][i] = "#"
        change.add((r, i))
        i -= 1

    i = c + 1
    while i < W and board_copy[r][i] != "#":
        board_copy[r][i] = "#"
        change.add((r, i))
        i += 1

    i = r + 1
    while i < H and board_copy[i][c] != "#":
        board_copy[i][c] = "#"
        change.add((i, c))
        i += 1
    return change

def restore(change):
    for r, c in change:
        board_copy[r][c] = board_auth[r][c]


def backtrack(r:int, c:int):
    nxt 