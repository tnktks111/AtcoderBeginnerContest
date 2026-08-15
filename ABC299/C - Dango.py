n = int(input())
S = input()
if "-" not in S or "o" not in S:
    print(-1)
    exit()
dango_sections = S.split("-")
res = 0
for dango_section in dango_sections:
    res = max(res, len(dango_section))
print(res)

