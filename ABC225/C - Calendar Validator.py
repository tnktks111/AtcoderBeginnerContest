N, M = map(int, input().split())

def line_validater(line):
    for i in range(len(line) - 1):
        if line[i] + 1 != line[i + 1]:
            return False
    return ((line[0] - 1) % 7 <= (line[-1] - 1) % 7)

prev_head = -1
for _ in range(N):
    line = list(map(int, input().split()))
    if (prev_head != -1 and prev_head + 7 != line[0]) or not line_validater(line):
        print("No")
        exit()
    prev_head = line[0]

print("Yes")