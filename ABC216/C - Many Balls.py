N = int(input())
rev_str = []
while (N):
	if N % 2 == 0:
		rev_str.append("B")
		N //= 2
	else:
		rev_str.append("A")
		N -= 1
rev_str.reverse()
print("".join(rev_str))