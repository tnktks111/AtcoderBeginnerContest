S = input()

if len(S) == 1:
    print(S)
    print(S)
    exit()

def shift_left(s: str):
    return s[1:] + s[0]

cur_max, cur_min = S, S
for _ in range(len(S) - 1):
    S = shift_left(S)
    if S > cur_max:
        cur_max = S
    if S < cur_min:
        cur_min = S
print(cur_min)
print(cur_max)