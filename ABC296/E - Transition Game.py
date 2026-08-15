#強連結成分分解が使えるらしい
N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1

seen = [0] * N
cycle_nodes_count = 0

for i in range(N):
    if seen[i] != 0:
        continue
    
    path = []
    curr = i
    
    while seen[curr] == 0:
        seen[curr] = 1
        path.append(curr)
        curr = A[curr]
    
    if seen[curr] == 1:
        cycle_len = 0
        for j in range(len(path) - 1, -1, -1):
            cycle_len += 1
            if path[j] == curr:
                break
        cycle_nodes_count += cycle_len

    for node in path:
        seen[node] = 2

print(cycle_nodes_count)

# N = int(input())
# A = list(map(int, input().split()))
# for i in range(N):
#     A[i] -= 1
# not_cycle = set()
# seen = set()
# for i in range(N):
#     if i in seen:
#         continue
#     seen.add(i)
#     slow, fast = A[i], A[A[i]]
#     junction = None
#     while slow != fast:
#         if slow in seen:
#             junction = slow
#             break
#         seen.add(slow)
#         slow = A[slow]
#         fast = A[A[fast]]
#     if junction:
#         slow2 = i
#         while slow2 != junction:
#             not_cycle.add(slow2)
#             slow2 = A[slow2]
#     else:
#         slow2 = i
#         while slow != slow2:
#             seen.add(slow)
#             not_cycle.add(slow2)
#             slow = A[slow]
#             slow2 = A[slow2]
# print(N - len(not_cycle))