S, T = input(), input()
n = len(S)
if n == 1:
    print("Yes")
    exit()
else:
    if ord(T[0]) - ord(S[0]) >= 0:
        K = ord(T[0]) - ord(S[0])
    else:
        K = ord(T[0]) - ord(S[0]) + 26
    for i in range(n):
        if (ord(S[i]) + K > 122 and chr(ord(S[i]) + K - 26) != T[i]) or (ord(S[i]) + K <= 122 and chr(ord(S[i]) + K) != T[i]):
            print("No")
            exit()
    print("Yes")
    