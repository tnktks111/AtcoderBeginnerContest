N = int(input())

square_list = []
i = 1
for i in range(1, N + 1):
    square_list.append(i ** 2)

def find_f_square(n:int):
    for i in range(1, len(square_list)):
        if n % square_list[i] == 0:
            return (square_list[i] * find_f_square(n // square_list[i]))
        if square_list[i] > n:
            break
    return 1

def nibutan(n:int) -> int:
    if n == square_list[-1]:
        return len(square_list)
    l, r = 0, len(square_list) - 1
    while (r - l > 1):
        m = (l + r) // 2
        if square_list[m] <= n:
            l = m
        else:
            r = m
    return l + 1

res = 0
for i in range(1, N + 1):
    j = i // find_f_square(i)
    res += nibutan(N // j)
print(res)