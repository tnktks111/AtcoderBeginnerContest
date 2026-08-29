S = input()
Q = int(input())
K = list(map(int, input().split()))

len_s = len(S)
# s l l s l s s l l s s l s l l s

def _islower(i:int, default):
    if i == 0:
        return default
    mask = 1 << (i.bit_length() - 1)
    return not _islower(i % mask, default)

def solve(idx:int):
    p, q = divmod(len_s, idx)
    char = S[q]
    if _islower(q, char.islower()):
        return char.lower()
    else:
        return char.upper()


    