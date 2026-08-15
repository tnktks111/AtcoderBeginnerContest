H, W = map(int, input().split())
A, B = [], []
possible_maps = []

for _ in range(H):
    A.append(list(input()))
for _ in range(H):
    B.append(tuple(input()))
B = tuple(B)

A_tmp = A[:]
for h in range(H):
    A_tmp = A[h:] + A[:h]
    for w in range(W):
        A_res = []
        for row in A_tmp:
            A_res.append(tuple(row[w:] + row[:w]))
        A_res = tuple(A_res)
        # print("_______________________")
        # print(A_res)
        # print("_______________________")
        if A_res == B:
            print("Yes")
            exit()
print("No")

