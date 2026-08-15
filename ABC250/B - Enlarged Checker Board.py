N, A, B = map(int, input().split())
line1 = ["."] * (N * B)
line2 = ["."] * (N * B)

for i in range(N):
    for j in range(B):
        if i % 2 == 0:
            line2[i * B + j] = "#"
        else:
            line1[i * B + j] = "#"
line1 = "".join(line1)
line2 = "".join(line2)

for i in range(N):
    for _ in range(A):
        print(line1 if i % 2 == 0 else line2)
