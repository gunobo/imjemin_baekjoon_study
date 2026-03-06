import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve():
    n, m, A, B = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    nodes = []
    
    for i in range(1, n + 1):
        x, y = map(int, input().split())
        nodes.append((x, y, i))
    
    for _ in range(m):
        u, v, k = map(int, input().split())
        adj[u].append(v)
        if k == 2:
            adj[v].append(u)

    dfn = [-1] * (n + 1)
    low = [-1] * (n + 1)
    stack = []
    in_stack = [False] * (n + 1)
    scc_id = [-1] * (n + 1)
    timer = 0
    scc_cnt = 0

    def tarjan(u):
        nonlocal timer, scc_cnt
        dfn[u] = low[u] = timer
        timer += 1
        stack.append(u)
        in_stack[u] = True
        
        for v in adj[u]:
            if dfn[v] == -1:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])
        
        if low[u] == dfn[u]:
            while True:
                node = stack.pop()
                in_stack[node] = False
                scc_id[node] = scc_cnt
                if node == u: break
            scc_cnt += 1

    for i in range(1, n + 1):
        if dfn[i] == -1:
            tarjan(i)

    scc_adj = [set() for _ in range(scc_cnt)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_adj[scc_id[u]].add(scc_id[v])

    west_nodes = sorted([n_info for n_info in nodes if n_info[0] == 0], key=lambda x: -x[1])
    east_nodes = sorted([n_info for n_info in nodes if n_info[0] == A], key=lambda x: -x[1])

    # 1. 서쪽에서 도달 가능한 SCC 찾기
    reachable = [False] * scc_cnt
    q = [scc_id[node[2]] for node in west_nodes]
    for s_id in q: reachable[s_id] = True
    
    curr = 0
    while curr < len(q):
        u = q[curr]
        curr += 1
        for v in scc_adj[u]:
            if not reachable[v]:
                reachable[v] = True
                q.append(v)

    # 2. 도달 가능한 동쪽 노드들의 SCC에 순차적으로 Rank 부여
    scc_min = [float('inf')] * scc_cnt
    scc_max = [float('-inf')] * scc_cnt
    
    valid_east_count = 0
    last_scc = -1
    for _, _, i in east_nodes:
        sid = scc_id[i]
        if reachable[sid]:
            valid_east_count += 1
            scc_min[sid] = min(scc_min[sid], valid_east_count)
            scc_max[sid] = max(scc_max[sid], valid_east_count)

    # 3. 위상 정렬을 통한 구간 전파
    in_deg = [0] * scc_cnt
    for u in range(scc_cnt):
        for v in scc_adj[u]:
            in_deg[v] += 1
            
    order = []
    topo_q = [i for i in range(scc_cnt) if in_deg[i] == 0]
    while topo_q:
        u = topo_q.pop()
        order.append(u)
        for v in scc_adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                topo_q.append(v)

    for u in reversed(order):
        for v in scc_adj[u]:
            scc_min[u] = min(scc_min[u], scc_min[v])
            scc_max[u] = max(scc_max[u], scc_max[v])

    # 4. 결과 출력
    for _, _, i in west_nodes:
        sid = scc_id[i]
        if scc_min[sid] == float('inf'):
            print(0)
        else:
            print(scc_max[sid] - scc_min[sid] + 1)

solve()