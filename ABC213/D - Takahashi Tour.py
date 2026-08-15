N = int(input())
adj = [[] for _ in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    adj[A - 1].append(B - 1)
    adj[B - 1].append(A - 1)

for i in range(N):
    adj[i].sort()
    
def EulerTour(n, adj, i0):
    stack = [i0]
    ET = []
    visit = [0] * N
    next_idx = [0] * N  # 各ノードの次に訪問する子のインデックスを追跡
    
    while stack:
        curr = stack[-1]
        
        if not visit[curr]:
            ET.append(curr + 1)
            visit[curr] = 1
        
        # 未訪問の隣接ノードがあるか確認
        while next_idx[curr] < len(adj[curr]) and visit[adj[curr][next_idx[curr]]]:
            next_idx[curr] += 1
        
        if next_idx[curr] < len(adj[curr]):
            # 未訪問の隣接ノードが見つかった
            next_node = adj[curr][next_idx[curr]]
            next_idx[curr] += 1
            stack.append(next_node)
        else:
            # すべての隣接ノードを訪問済み
            stack.pop()
            # 親ノードに戻った場合のみ出力
            if stack:
                ET.append(stack[-1] + 1)
    
    return ET

print(*EulerTour(N, adj, 0))