X = input()
N = int(input())
S = [input() for _ in range(N)]
def_to_base = {chr(97 + i): X[i] for i in range(26)}
base_to_def = {X[i]: chr(97 + i) for i in range(26)}
def conv_strbase(s, base):
	res = []
	for i in range(len(s)):
		res.append(base[s[i]])
	return ("".join(res))
S_def = [conv_strbase(s, base_to_def) for s in S]
S_def_sorted = sorted(S_def)
for s in S_def_sorted:
    print(conv_strbase(s, def_to_base))
