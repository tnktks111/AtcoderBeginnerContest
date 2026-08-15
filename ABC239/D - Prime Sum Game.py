A, B, C, D = map(int, input().split())
def is_prime(n:int) -> bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 5 or n == 7:
        return True
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True
for T in range(A, B + 1):
    t_win = True
    for A in range(C, D + 1):
        if is_prime(T + A):
            t_win = False
            break
    if t_win:
        break
print("Takahashi" if t_win else "Aoki")