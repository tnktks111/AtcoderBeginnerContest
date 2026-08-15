A, B, C, D, E, F, X = map(int, input().split())

tak_len = A * B * (X // (A + C)) + min(X % (A + C), A) * B
aok_len = D * E * (X // (D + F)) + min(X % (D + F), D) * E
if tak_len > aok_len:
    print("Takahashi")
elif aok_len > tak_len:
    print("Aoki")
else:
    print("Draw")