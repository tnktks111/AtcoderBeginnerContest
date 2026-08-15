upp_chr = set([chr(i) for i in range(65, 91)])
low_chr = set([chr(i) for i in range(97, 123)])
S = input()
if len(S) != len(set(S)) or not (set(S) & upp_chr) or not (set(S) & low_chr):
    print("No")
else:
    print("Yes")

# import sys

# s=input().strip()
# if s=="":
#     sys.exit(0)
# if len(set(list(s))) == len(s):
#     a,b=False,False
#     for c in s:
#         if c>='a' and c<='z': a=True
#         if c>='A' and c<='Z': b=True
#     if a and b: print("Yes")
#     else: print("No")
# else:
#     print("No")