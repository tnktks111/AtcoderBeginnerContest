N = int(input())
A = list(map(int, input().split()))
res = [n for n in A if n % 2 == 0]
print(*res)