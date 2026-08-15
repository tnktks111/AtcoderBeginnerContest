A, B = map(int, input().split())
a = sorted(list(set(map(int, input().split()))))
b = sorted(list(set(map(int, input().split()))))
k = l = 0
cur_min = float('inf')

while k < len(a) and l < len(b):
    cur_min = min(cur_min, abs(a[k] - b[l]))
    if a[k] < b[l]:
        k += 1
    else:
        l += 1
print(cur_min)