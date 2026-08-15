S = input()

def is_palindrome(s:str):
    if s == s[::-1]:
        return True
    else:
        return False

l, r = 0, len(S) - 1
while r > 0 and S[r] == "a":
    r -= 1

if r == 0:
    print("Yes")
    exit()

while l < len(S) - 1 and S[l] == "a":
    l += 1

if (len(S) - 1) - r < l:
    print("No")
elif is_palindrome(S[l:r + 1]):
    print("Yes")
else:
    print("No")