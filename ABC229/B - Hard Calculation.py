A, B = map(int, input().split())
while A and B:
    a, b = A % 10, B % 10
    if a + b > 9:
        print("Hard")
        exit()
    A //= 10
    B //= 10
print("Easy")