import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    A, B, N = map(int, input().split())
    
    diffs = list({A, B})
    
    # 간선: adj[v]를 스택으로 관리 (쌍방향 삭제를 위해 edge_id 사용)
    edges = []
    # adj[v] = list of edge_id
    adj = [[] for _ in range(N + 1)]
    deg = [0] * (N + 1)
    
    for d in diffs:
        for x in range(1, N - d + 1):
            y = x + d
            eid = len(edges)
            edges.append((x, y))
            adj[x].append(eid)
            adj[y].append(eid)
            deg[x] += 1
            deg[y] += 1
    
    total_edges = len(edges)
    
    if total_edges == 0:
        if N == 1:
            sys.stdout.write('1\n1\n')
        else:
            sys.stdout.write('-1\n')
        return
    
    for v in range(1, N + 1):
        if deg[v] == 0:
            sys.stdout.write('-1\n')
            return
    
    odd = [v for v in range(1, N + 1) if deg[v] % 2 == 1]
    if len(odd) not in (0, 2):
        sys.stdout.write('-1\n')
        return
    
    # 연결성 확인 (간선 있는 노드들)
    visited = bytearray(N + 1)
    stack = [1]
    visited[1] = 1
    cnt = 1
    while stack:
        v = stack.pop()
        for eid in adj[v]:
            u = edges[eid][0] if edges[eid][1] == v else edges[eid][1]
            if not visited[u]:
                visited[u] = 1
                cnt += 1
                stack.append(u)
    if cnt != N:
        sys.stdout.write('-1\n')
        return
    
    # Hierholzer: adj_idx로 O(1) 포인터 이동 + used_edge 배열
    used = bytearray(total_edges)
    adj_ptr = [0] * (N + 1)
    
    start = odd[0] if odd else 1
    path = []
    stk = [start]
    
    while stk:
        v = stk[-1]
        found = False
        while adj_ptr[v] < len(adj[v]):
            eid = adj[v][adj_ptr[v]]
            adj_ptr[v] += 1
            if not used[eid]:
                used[eid] = 1
                u = edges[eid][0] if edges[eid][1] == v else edges[eid][1]
                stk.append(u)
                found = True
                break
        if not found:
            path.append(stk.pop())
    
    if len(path) != total_edges + 1:
        sys.stdout.write('-1\n')
        return
    
    out = [str(len(path)), ' '.join(map(str, path))]
    sys.stdout.write('\n'.join(out) + '\n')

solve()