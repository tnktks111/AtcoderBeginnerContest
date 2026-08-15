# N, K = map(int, input().split())
# A, B = list(map(int, input().split())), list(map(int, input().split()))
# DP = [[False, False] for _ in range(N)]
# DP[0][0] = DP[0][1] = True
# for i in range(N - 1):
#     if DP[i][0]:
#         if abs(A[i + 1] - A[i]) <= K:
#             DP[i+1][0] = True
#         if abs(B[i + 1] - A[i]) <= K:
#             DP[i+1][1] = True
#     if DP[i][1]:
#         if abs(A[i + 1] - B[i]) <= K:
#             DP[i+1][0] = True
#         if abs(B[i + 1] - B[i]) <= K:
#             DP[i+1][1] = True
# print("Yes" if DP[N - 1][0] or DP[N - 1][1] else "No")

N, K = map(int, input().split())
A, B = list(map(int, input().split())), list(map(int, input().split()))

for i in range(N - 1):
    if (A[i + 1] < A[i] - K or A[i + 1] > A[i] + K) and (A[i + 1] < B[i] - K or A[i + 1] > B[i] + K):
        A[i + 1] = float("inf")
    if (B[i + 1] < A[i] - K or B[i + 1] > A[i] + K) and (B[i + 1] < B[i] - K or B[i + 1] > B[i] + K):
        B[i + 1] = float("inf")
print("Yes" if A[N - 1] != float("inf") or B[N - 1] != float("inf") else "No")