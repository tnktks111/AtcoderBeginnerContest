from collections import deque
N, Q = map(int, input().split())

#次に呼ばれる人
wait = 1

#呼ばれた人
called = [False] * N

#再度呼ばれる人
recall = 1

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        wait += 1
    elif query[0] == 2:
        called[query[1] - 1] = True
    else:
        while called[recall - 1] == True:
            recall += 1
        print(recall)