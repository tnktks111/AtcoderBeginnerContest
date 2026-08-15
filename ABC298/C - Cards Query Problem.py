from sortedcontainers import SortedSet, SortedList
from collections import defaultdict
N = int(input())
Q = int(input())

box_to_items = defaultdict(SortedList)
item_to_boxes = defaultdict(SortedSet)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        box_to_items[query[2]].add(query[1])
        item_to_boxes[query[1]].add(query[2])
    elif query[0] == 2:
        print(*box_to_items[query[1]])
    elif query[0] == 3:
        print(*item_to_boxes[query[1]])
