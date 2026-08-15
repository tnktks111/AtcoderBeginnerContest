S = input()
T = input()
head_S = [False] * (len(T) + 1)
tail_S = [False] * (len(T) + 1)

head_S[0] = True
for i in range(1, len(T) + 1):
    if head_S[i - 1] == True and (S[i - 1] == T[i - 1] or S[i - 1] == "?" or T[i - 1] == "?"):
        head_S[i] = True
    else:
        break
tail_S[0] = True
for i in range(1, len(T) + 1):
    if tail_S[i - 1] == True and (S[-i] == T[-i] or S[-i] == "?" or T[-i] == "?"):
        tail_S[i] = True
    else:
        break
for i in range(len(T) + 1):
    if head_S[i] and tail_S[len(T) - i]:
        print("Yes")
    else:
        print("No")
