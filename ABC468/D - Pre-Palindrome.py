S = input()
N = len(S)

res = 0
for i in range(N):
    j = 0
    wrong_cnt = 0
    while True:
        if i - j < 0 or i + j >= N:
            break
        if S[i - j] != S[i + j]:
            wrong_cnt += 1
        if wrong_cnt == 2:
            break
        res += 1
        j += 1

for i in range(N - 1):
    j = 0
    wrong_cnt = 0
    while True:
        if i - j < 0 or i + j + 1 >= N:
            break
        if S[i - j] != S[i + j + 1]:
            wrong_cnt += 1
        if wrong_cnt == 2:
            break
        res += 1
        j += 1

print(res)