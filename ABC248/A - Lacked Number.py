S = input()
nums = set(range(10))
for i in range(9):
    nums.remove(int(S[i]))
print(list(nums)[0])