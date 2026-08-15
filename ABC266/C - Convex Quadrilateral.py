
def vec2d_cross_z(p:tuple[int, int], q:tuple[int, int]):
    return p[0] * q[1] - p[1] * q[0]

def vec2d(start:tuple[int, int], end:tuple[int, int]):
    return (end[0] - start[0], end[1] - start[1])

def is_in_triangle(P:tuple[int, int], triangle:tuple[tuple[int, int], tuple[int, int], tuple[int, int]]):
    a, b, c = triangle
    AP_AB_z = vec2d_cross_z(vec2d(a, P), vec2d(a, b))
    BP_BC_z = vec2d_cross_z(vec2d(b, P), vec2d(b, c))
    CP_CA_z = vec2d_cross_z(vec2d(c, P), vec2d(c, a))
    if AP_AB_z > 0 and BP_BC_z > 0 and CP_CA_z > 0:
        return True
    if AP_AB_z < 0 and BP_BC_z < 0 and CP_CA_z < 0:
        return True
    return False

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))
D = tuple(map(int, input().split()))

if is_in_triangle(D, (A, B, C)) or is_in_triangle(A, (B, C, D)) or is_in_triangle(B, (C, D, A)) or is_in_triangle(C, (D, A, B)):
    print("No")
else:
    print("Yes")