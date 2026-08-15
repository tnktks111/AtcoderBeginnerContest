points = list(map(int, input().split()))
given_diff = (abs(points[0]-points[2]), abs(points[1]-points[3]))
diff = {(0,0), (0,2), (0,4), (1,1), (1,3), (2,0), (2,4), (3,1), (3,3), (4,0), (4,2)}
if given_diff in diff:
    print("Yes")
else:
    print("No")