N, X, Y = map(int, input().split())

bus_stops = [tuple(map(int, input().split())) for _ in range(N - 1)]

def calc_time(start: int):
    t_cur = start + X
    for (p, t) in bus_stops:
        divisor, remainder = divmod(t_cur, p)
        if remainder:
            t_cur = (divisor + 1) * p + t
        else:
            t_cur = t_cur + t
    return t_cur + Y

modulo2time = [0] * 840
for i in range(840):
    modulo2time[i] = calc_time(i)

Q = int(input())
for _ in range(Q):
    q = int(input())
    divisor, remainder = divmod(q, 840)
    print(modulo2time[remainder] + divisor * 840)