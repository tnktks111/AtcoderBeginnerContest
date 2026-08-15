import collections
int(input())
S = input()
seen = set()

curr = [0, 0]
seen.add(tuple(curr))
for i in range(len(S)):
    if S[i] == "R":
        curr[0] += 1
    elif S[i] == "L":
        curr[0] -= 1
    elif S[i] == "U":
        curr[1] += 1
    else:
        curr[1] -= 1
    # print(tuple(curr))
    if tuple(curr) in seen:
        print("Yes")
        exit()
    seen.add(tuple(curr))
print("No")