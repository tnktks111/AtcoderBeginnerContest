S, T = map(int, input().split())
a = 0
def dfs(a, b, c, K, L, seen):
	if (a < b or b < c or a + b + c > K or a * b * c > L or (a, b, c) in seen):
		return 0
	seen.add((a, b ,c))
	if a == b == c:
		return 1 + dfs(a + 1, b, c, K, L, seen) + dfs(a, b + 1, c, K, L, seen) + dfs(a, b, c + 	1, K, L, seen)
	elif a == b or b == c or c == a:
		return 3 + dfs(a + 1, b, c, K, L, seen) + dfs(a, b + 1, c, K, L, seen) + dfs(a, b, c + 	1, K, L, seen)
	else:
		return 6 + dfs(a + 1, b, c, K, L, seen) + dfs(a, b + 1, c, K, L, seen) + dfs(a, b, c + 	1, K, L, seen)
seen = set()
print(dfs(0, 0, 0, S, T, seen))