K = int(input())
A, B = input().split()

def convert_base(n: str, base: int):
    res = 0
    i = 0
    while (i < len(n)):
        res = res * base + (int(n[i]))
        i += 1
    return (res)

print(convert_base(A, K) * convert_base(B, K))