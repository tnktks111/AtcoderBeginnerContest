from collections import deque
N, Q = map(int, input().split())
prv = [-1] * N
nxt = [-1] * N
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        nxt[query[1] - 1] = query[2]
        prv[query[2] - 1] = query[1]
    elif query[0] == 2:
        nxt[query[1] - 1] = -1
        prv[query[2] - 1] = -1
    else:
        cur = query[1]
        res = deque()
        while (prv[cur - 1] != -1):
            res.appendleft(prv[cur - 1])
            cur = prv[cur - 1]
        cur = query[1]
        res.append(cur)
        while (nxt[cur - 1] != -1):
            res.append(nxt[cur - 1])
            cur = nxt[cur - 1]
        res.appendleft(len(res))
        print(" ".join(map(str, res)))
        
        

# 頑張ってlinkedlist使おうとしたもののTLEになってしまった
# from collections import deque
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.parent = self
#         self.prev = self.next = None

# class Train:
#     def __init__(self, num:int):
#         self.nodes = {}
#         for i in range(num):
#             self.nodes[i+1] = Node(i+1)
    
#     def connect(self, prv: Node, nxt: Node):
#         prv.next = nxt
#         nxt.prev = prv
#         cur = nxt
#         while cur:
#             cur.parent = prv.parent
#             cur = cur.next

#     def separate(self, prv: Node, nxt: Node):
#         prv.next = None
#         nxt.prev = None
        
#         cur = nxt
#         while cur:
#             cur.parent = nxt
#             cur = cur.next

# N, Q = map(int, input().split())
# trains = Train(N)
# for _ in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         trains.connect(trains.nodes[query[1]], trains.nodes[query[2]])
#     elif query[0] == 2:
#         trains.separate(trains.nodes[query[1]], trains.nodes[query[2]])
#     else:
#         cur = trains.nodes[query[1]].parent
#         res = deque()
#         cnt = 0
#         while cur:
#             res.append(cur.val)
#             cur = cur.next
#             cnt += 1
#         res.appendleft(cnt)
#         print(" ".join(map(str, res)))

