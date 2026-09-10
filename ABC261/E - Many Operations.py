N, C = map(int, input().split())

prv = C

pattern_zeros = 0
pattern_ones = (1 << 30) - 1

for _ in range(N):
    t, a = map(int, input().split())
    match t:
        case 1:
            pattern_zeros &= a
            pattern_ones &= a
        case 2:
            pattern_zeros |= a
            pattern_ones |= a
        case 3:
            pattern_zeros ^= a
            pattern_ones ^= a

    nxt = 0
    for i in range(30):
        if (1 << i) & prv:
            nxt |= (1 << i) & pattern_ones 
        else:
            nxt |= (1 << i) & pattern_zeros
    print(nxt)
    prv = nxt

