from itertools import permutations

S, K = input().split()
K = int(K)
perm = sorted(set(permutations(S)))
print("".join(perm[K - 1]))

# from typing import List

# S, K = input().split()
# K = int(K)
# S_set = sorted(set(S))
# CToN = {S_set[i]: i for i in range(len(S_set))}
# nums = [CToN[s] for s in S]
# def permute(nums: List[int]) -> List[List[int]]:
# 	def backtrack(start):
# 		if start == len(nums):
# 			if nums[:] not in result:
# 				result.append(nums[:])
# 			return
# 		for i in range(start, len(nums)):
# 			nums[start], nums[i] = nums[i], nums[start]
# 			backtrack(start + 1)
# 			nums[start], nums[i] = nums[i], nums[start]
# 	result = []
# 	backtrack(0)
# 	return result

# resNum = sorted(permute(nums))[K - 1]
# resChar = [S_set[c] for c in resNum]
# print("".join(resChar))
