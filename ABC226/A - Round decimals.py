X = float(input())

def my_round(n:float):
    if (n * 10) % 10 >= 5:
        return int(n + 1)
    else:
        return int(n)

print(my_round(X))