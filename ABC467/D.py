def solve(px, py, qx, qy, rx, ry, sx, sy):
    gen_vec_1 = (px - qx, py - qy)
    gen_mid_1 = ((px + qx) / 2, (py + qy) / 2)
    gen_vec_2 = (rx - sx, ry - sy)
    gen_mid_2 = ((rx + sx) / 2, (ry + sy) / 2)
    mid_vec = (gen_mid_1[0] - gen_mid_2[0], gen_mid_1[1] - gen_mid_2[1])
    if gen_vec_1[0] * gen_vec_2[1] - gen_vec_1[1] * gen_vec_2[0] != 0:
        return True
    if gen_vec_1[0] * mid_vec[0] + gen_vec_1[1] * mid_vec[1] == 0:
        return True
    return False

T = int(input())

for _ in range(T):
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())
    print("Yes" if solve(px, py, qx, qy, rx, ry, sx, sy) else "No")