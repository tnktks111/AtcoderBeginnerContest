import math

T = int(input())

def solve(n:int, x:int, k:int):
    # print(f"n:{n}, x:{x}, k:{k}")
    cur = x
    res = 0
    under_dist = k
    seen = set()

    height = math.ceil(math.log2(n + 1))
    max_dist = 2 * (height - 1)

    while cur > 0 and under_dist >= 0:
        if under_dist > max_dist:
            child_cnt = 0
        elif under_dist > 0:
            left_child = cur * 2
            right_child = cur * 2 + 1
            child_cnt = 0
            child_dist = under_dist - 1
            if left_child not in seen:
                child_cnt += max(min(n, (left_child + 1) * 2 ** child_dist - 1) - (left_child * 2 ** child_dist) + 1, 0)
            if right_child not in seen:
                child_cnt += max(min(n, (right_child + 1) * 2 ** child_dist - 1) - (right_child * 2 ** child_dist) + 1, 0)
            # print("child", child_cnt)
        else:
            child_cnt = 1
        res += child_cnt
        seen.add(cur)
        # print(f"cur: {cur}, child_cnt: {child_cnt}, under_dist: {under_dist}")
        cur //= 2
        under_dist -= 1
    return res

for _ in range(T):
    n, x, k = map(int, input().split())
    print(solve(n, x, k))