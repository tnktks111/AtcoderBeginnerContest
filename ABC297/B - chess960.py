from collections import defaultdict
S = input()
c_to_idx = defaultdict(list)

for i in range(8):
    c_to_idx[S[i]].append(i)

if c_to_idx["B"][0]%2 == c_to_idx["B"][1]%2:
    print("No")
    exit()
if c_to_idx["R"][0] < c_to_idx["K"][0] < c_to_idx["R"][1]:
    print("Yes")
    exit()
print("No")