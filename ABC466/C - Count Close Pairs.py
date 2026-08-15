N = int(input())

res = 0
j = 2

for i in range(1, N):
    if j <= i:
        j = i + 1
    while j <= N:
        print(f"? {i} {j}")
        ans = input()
        if ans == "No":
            break
        j += 1
    res += j - i - 1

print(f"! {res}")