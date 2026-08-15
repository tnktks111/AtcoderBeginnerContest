N = int(input())
A = list(map(int, input().split()))
X = int(input())

A_sum = sum(A)
div, mod = X // A_sum, X % A_sum
remain = 0
while(mod >= 0):
    mod -= A[remain]
    remain += 1
print(div * len(A) + remain)