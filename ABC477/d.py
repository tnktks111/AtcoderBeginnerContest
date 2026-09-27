N, Q = map(int, input().split())

masked = [False] * N
not_masked_set = set()
queries = [tuple(input().split()) for _ in range(Q)]
for i in range(Q):
    if queries[i][0] == "1":
        target = int(queries[i][1]) - 1
        masked[target] = True if not masked[target] else False
for i in range(N):
    if not masked[i]:
        not_masked_set.add(i)
 
queries.reverse()

res = [""] * N
remain = set(range(N))

for i in range(Q):
    qry = queries[i]
    if qry[0] == "1":
        target = int(qry[1]) - 1
        if res[target] != "":
            continue
        if masked[target] == True:
            masked[target] = False
            not_masked_set.add(target)
        else:
            masked[target] = True
            not_masked_set.remove(target)
    else:
        for i in not_masked_set:
            res[i] = qry[1]
        not_masked_set = set()

for i in range(N):
    if res[i] == "":
        res[i] = "a"

print("".join(res))