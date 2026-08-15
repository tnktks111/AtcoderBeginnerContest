N = int(input())
S = set(input().split())
target = {"and", "not", "that", "the", "you"}
if S & target:
    print("Yes")
else:
    print("No")