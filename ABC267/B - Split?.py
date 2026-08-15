S = input()
row = [
    S[6] == "1",
    S[3] == "1",
    S[1] == "1" or S[7] == "1",
    S[0] == "1" or S[4] == "1",
    S[2] == "1" or S[8] == "1",
    S[5] == "1",
    S[9] == "1" 
]

if S[0] == "1":
    print("No") 
else:
    left_exist = False
    empty_exist = False
    for i in range(7):
        if empty_exist:
            if row[i] == True:
                print("Yes")
                exit()
        else:
            if row[i] == True:
                left_exist = True
            elif left_exist == True:
                empty_exist = True
    print("No")