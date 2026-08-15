A, B, C = map(int, input().split())
a, b = A // C, B // C
if A % C == 0:
    print(A)
elif B % C == 0:
    print(B)
elif a == b:
    print(-1)
else:
    print(C * (a + 1))
