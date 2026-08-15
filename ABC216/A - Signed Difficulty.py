X, Y = map(int, input().split('.'))
if (0 <= Y <= 2):
	print(str(X)+'-')
if (3 <= Y <= 6):
	print(str(X))
if (7 <= Y <= 9):
	print(str(X)+'+')