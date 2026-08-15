A = input()
a = int(A[0])
b = int(A[1])
c = int(A[2])
d = int(A[3])
if (a == b == c == d
    or ((a + 1) % 10 == b and (b + 1) % 10 == c and (c + 1) % 10== d)):
	print("Weak")

else:
    print("Strong")