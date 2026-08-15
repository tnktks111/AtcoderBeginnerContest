H, W = map(int, input().split())
for _ in range(H):
    S = input().split(".")
    newS = []
    for ts in S:
        elem = list(ts)
        i = 0
        while i + 1 < len(elem):
            elem[i] = "P"
            elem[i + 1] = "C"
            i += 2
        newS.append("".join(elem))
    print(".".join(newS))
