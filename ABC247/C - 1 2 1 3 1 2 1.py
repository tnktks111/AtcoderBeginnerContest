N = int(input())

def print_rec(n:int):
    if n == 1:
        return [1]
    return (print_rec(n - 1) + [n] + print_rec(n - 1))
print(*print_rec(N))