N = int(input())
S = input()
res = 0

consective_R = S.split("S")
for chunk in consective_R:
    res = max(len(chunk), res)

print(res)