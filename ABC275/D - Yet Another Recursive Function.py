N = int(input())
memo = {}
def yet_another_recursive_func(x:int):
    if x == 0:
        return 1
    if x in memo:
        return memo[x]
    res = yet_another_recursive_func(x // 2) + yet_another_recursive_func(x // 3)
    memo[x] = res
    return res
print (yet_another_recursive_func(N))