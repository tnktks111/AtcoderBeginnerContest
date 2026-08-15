from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
candidates = list(permutations(range(1, N + 1)))

start_window = False
end_window = False

res = 0
for candidate in candidates:
    if candidate == Q:
        end_window = True
    if start_window and not end_window:
        res += 1
    if candidate == P:
        start_window = True
        
print(res)