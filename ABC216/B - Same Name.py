N = int(input())
Names = [input() for _ in range(N)]
if N != len(set(Names)):
	print("Yes")
else:
    print("No")