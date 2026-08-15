N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


A_set = set()
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            A_set.add((i, j))
# print(A_set)

if not A_set:
    print("Yes")
    exit()

B_set = set()
for i in range(N):
    for j in range(N):
        if B[i][j] == 1:
            B_set.add((i, j))

found = True
for elem in A_set:
    if elem not in B_set:
        found = False
        break
if found:
    print("Yes")
    exit()

for _ in range(3):
    A_tmp = set()
    found = True
    for i, j in A_set:
        A_tmp.add((j, N-1-i))
    # print(A_tmp)
    for elem in A_tmp:
        if elem not in B_set:
            found = False
            break
    if found:
        print("Yes")
        exit()
    A_set = A_tmp.copy()

print("No")