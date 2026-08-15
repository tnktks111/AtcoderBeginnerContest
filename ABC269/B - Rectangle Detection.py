S = list(input() for _ in range(10))

found = False
A, B, C, D = 0, 0, 0, 0
for i in range(10):
    if S[i] == "..........":
        continue
    B = i + 1
    if not found:
        found = True
        A = i + 1
        start = True
        for j in range(10):
            if S[i][j] == "#":
                if start:
                    start = False
                    C = j + 1
                D = j + 1
print (f"{A} {B}\n{C} {D}")