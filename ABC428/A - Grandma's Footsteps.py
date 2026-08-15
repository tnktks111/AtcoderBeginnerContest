S, A, B, X = map(int, input().split())
print((X // (A + B)) * (S * A) + min((X % (A + B)), A) * S)