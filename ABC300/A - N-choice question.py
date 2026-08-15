N, A, B = map(int, input().split())
C = list(map(int, input().split()))
choice_to_N = {C[i]: i + 1 for i in range(len(C))}
print(choice_to_N[A + B])