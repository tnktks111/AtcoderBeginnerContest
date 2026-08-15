import heapq
N, M = map(int, input().split())
hands = [input() for _ in range(2 * N)]

def RPS(myhand: str, opphand :str):
    if myhand == opphand:
        return 0
    elif (myhand == "G" and opphand == "C") or (myhand == "C" and opphand == "P") or (myhand == "P" and opphand == "G"):
        return -1
    else:
        return 0

Maxheap = []
for i in range(2 * N):
    heapq.heappush(Maxheap, (0, i))

for i in range(M):
    Newheap = []
    for _ in range(N):
        a_point, a_num = heapq.heappop(Maxheap)
        b_point, b_num = heapq.heappop(Maxheap)
        a_point += RPS(hands[a_num][i], hands[b_num][i])
        b_point += RPS(hands[b_num][i], hands[a_num][i])
        heapq.heappush(Newheap, (a_point, a_num))
        heapq.heappush(Newheap, (b_point, b_num))
    Maxheap = Newheap

for i in range(2 * N):
    print(1 + heapq.heappop(Maxheap)[1])