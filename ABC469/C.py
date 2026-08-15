N = int(input())
S = input()

# res = []
# for k in range(1, N + 1):
#     have = 0
#     eat = k
#     for i in range(k):
#         if S[i] == "o":
#             have += 1
#     l = k
#     while l < N and have > 0:
#         if S[l] == "o":
#             have += 1
#         eat += 1
#         have -= 1
#         l += 1
#     res.append(eat)
# print(res)

check = [1] * (N + 1)
k2num = dict()
for i in range(N):
    if i == 0 or S[i - 1] == "o":
        check[i + 1] = check[i]
    else:
        check[i + 1] = check[i] + 1
        k2num[check[i]] = i

res = []
for i in range(1, N + 1):
    if i in k2num:
        res.append(k2num[i])
    else:
        res.append(N)
print(*res, sep="\n")