A, B, C, D = map(int, input().split())
print("No" if (A <= C and B <= D) or (A > C) else "Yes")