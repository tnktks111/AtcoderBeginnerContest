N, K = map(int, input().split())
A = list(map(int, input().split()))

sorted_A = sorted(A)

window_start = None

# print(A)
# print(sorted_A)
for i in range(N):
    if A[i] != sorted_A[i]:
        if window_start is None:
            window_start = i
        else:
            if window_start + K - 1 < i:
                print("No")
                # print(window_start, i)
                exit()
            else:
                continue

print("Yes")