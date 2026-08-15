from typing import List
import heapq

N = input()
NumList = [-int(n) for n in N]
heapq.heapify(NumList)

def backtrack(s: int, t: int, remain: List[int]):
    if not remain:
        curMax[0] = max(s * t, curMax[0])
        return
    a = -heapq.heappop(remain)
    if not (a == 0 and s == 0):
        backtrack(s * 10 + a, t, remain.copy())
    if not (a == 0 and t == 0):
        backtrack(s, t * 10 + a, remain.copy())
        
curMax = [0]
backtrack(0, 0, NumList)

print(curMax[0])