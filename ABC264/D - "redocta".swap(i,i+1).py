S = input()
res = 0
c_to_num = {"a":0, "t":1, "c":2, "o":3, "d":4, "e":5, "r":6}
rec = [0] * 7
for i in range(7):
    res += rec[c_to_num[S[i]]]
    for j in range(c_to_num[S[i]]):
        rec[j] += 1
print(res)