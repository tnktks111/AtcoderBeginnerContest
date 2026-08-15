from collections import deque
#0:上,1:右,2:下,3:左
dir_num_to_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
A_non_cost_dir = [0, 1, 2, 3]
B_non_cost_dir = [3, 2, 1, 0]
C_non_cost_dir = [1, 0, 3, 2]
A_nxt_dir = []
B_nxt_dir = []
C_nxt_dir = []
def solve(H:int, W:int, s:list[str]):
    dp = [[[float("inf")] * 4 for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append((0, 0, -1, 1))
    while q:
        cur_cost, h, w, cur_dir_num = q.popleft()
        dh, dw = dir_num_to_dir[cur_dir_num]
        nh, nw = h + dh, w + dw
        if nh == H and nw == W:
            break
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        A_dirnum = A_non_cost_dir[cur_dir_num]
        B_dirnum = B_non_cost_dir[cur_dir_num]
        C_dirnum = C_non_cost_dir[cur_dir_num]
        A_cost, B_cost, C_cost = cur_cost + 1, cur_cost + 1, cur_cost + 1
        if s[nh][nw] == "A":
            A_cost -= 1
        elif s[nh][nw] == "B":
            B_cost -= 1
        else:
            C_cost -= 1
        if dp[nh][nw][A_dirnum] > A_cost:
            dp[nh][nw][A_dirnum] = A_cost
            if s[nh][nw] == "A":
                q.appendleft((A_cost, nh, nw, A_dirnum))
            else:
                q.append((A_cost, nh, nw, A_dirnum))
        if dp[nh][nw][B_dirnum] > B_cost:
            dp[nh][nw][B_dirnum] = B_cost
            if s[nh][nw] == "B":
                q.appendleft((B_cost, nh, nw, B_dirnum))
            else:
                q.append((B_cost, nh, nw, B_dirnum))
        if dp[nh][nw][C_dirnum] > C_cost:
            dp[nh][nw][C_dirnum] = C_cost
            if s[nh][nw] == "C":
                q.appendleft((C_cost, nh, nw, C_dirnum))
            else:
                q.append((C_cost, nh, nw, C_dirnum))
    return dp[H - 1][W - 1][1]

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    res = solve(H, W, list(input() for _ in range(H)))
    print(res)