pinacles = {"v":1, "w":2}
S = input()
res = 0
for c in S:
    res += pinacles[c]
print(res)