from sortedcontainers import SortedList
import bisect
N = int(input())
X = list(map(int, input().split()))

line = SortedList([0, X[0]])
tmp = X[0] * 2
print(tmp)
if N >= 2:
    if X[1] > X[0]:
        tmp += X[1] - X[0]
        if X[1] - X[0] < X[0]:
            tmp = tmp - X[0] + (X[1] - X[0]) 
    else:
        tmp += min(X[0] - X[1], X[1])
        tmp -= X[0]
    line.add(X[1])
    print(tmp)
    for i in range(2, N):
        l = line.bisect_left(X[i])
        # 右端に入れる場合
        if l == i + 1:
            tmp += (X[i] - line[-1])
            if line[-1] - line[-2] > X[i] - line[-1]:
                tmp = tmp + (X[i] - line[-1]) - (line[-1] - line[-2])
        else:
            RightVal = line[l]
            LeftVal = line[l - 1]
            tmp += min(X[i] - LeftVal, RightVal - X[i])
            # 右側の更新
            # 右端の区間に挿入する場合
            if l + 1 == i + 1:
                tmp = tmp + (RightVal - X[i]) - (RightVal - LeftVal)
            else:
                prev = min(RightVal - LeftVal, line[l + 1] - RightVal)
                if prev > RightVal - X[i]:
                    tmp = tmp + (RightVal - X[i]) - prev
            # 左側の更新
            # 左端の区間に挿入する場合
            if l - 1 == 0:
                tmp = tmp + (X[i] - LeftVal) - (RightVal - LeftVal)
            else:
                prev = min(LeftVal - line[l - 2], RightVal - LeftVal)
                if prev > X[i] - LeftVal:
                    tmp = tmp + (X[i] - LeftVal) - prev        
        line.add(X[i])
        print(tmp)