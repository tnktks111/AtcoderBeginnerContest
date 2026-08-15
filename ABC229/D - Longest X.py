S = input()
X = int(input())

N = len(S)
left = 0
right = 0
cur_modify = 0
cur_max = 0

while right < N:
    if S[right] == ".":
        cur_modify += 1

    while cur_modify > X:
        if S[left] == ".":
            cur_modify -= 1
        left += 1

    cur_max = max(cur_max, right - left + 1)
    right += 1

print(cur_max)
