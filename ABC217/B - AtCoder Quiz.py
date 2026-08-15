S_1 = input()
S_2 = input()
S_3 = input()
contests = {"ABC", "ARC", "AGC", "AHC"}
contests.difference_update({S_1, S_2, S_3})
print(contests.pop())