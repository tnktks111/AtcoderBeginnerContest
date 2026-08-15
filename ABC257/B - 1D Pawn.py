N, K, Q = map(int, input().split())
A = [0] + list(map(int, input().split())) #1-indexed
L = list(map(int, input().split()))
board = [False] * (N + 2) #1-indexed
board[N + 1] = True
for i in range(1, K + 1):
    board[A[i]] = True
for i in range(Q):
    if board[A[L[i]] + 1] == False:
        board[A[L[i]]] = False
        board[A[L[i]] + 1] = True
        A[L[i]] += 1
print(*A[1:])