from bisect import bisect_right
T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    A_essential = []
    prev = float("inf")
    for a in A:
        if prev > a:
            A_essential.append(a)
    A = A_essential
    A.reverse()

    p, q = divmod(x, A[-1])
    tmp_cycle = 1
    modulo = 0
    for i in range(1, len(A)):
        if A[i - 1] <= q < A[i]:
            modulo = tmp_cycle * (q // A[i - 1]) + bisect_right(A, q % A[i - 1])
        tmp_cycle = tmp_cycle * (A[i] // A[i - 1]) + 1

    print(p * tmp_cycle + modulo)
    