import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    H = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # 실력 기준 오름차순 정렬
    idx = sorted(range(N), key=lambda i: A[i])
    a = [A[idx[i]] for i in range(N)]
    h = [H[idx[i]] for i in range(N)]
    l = [L[idx[i]] for i in range(N)]

    # Min-Cost Max-Flow
    # 노드: S=0, 비우승자 j+1, 참가자 i+N+1, T=2N+1
    S = 0
    T = 2 * N + 1
    V = T + 1

    to = []; cap = []; cost = []; rev = []
    head = [[] for _ in range(V)]

    def add(u, v, c, w):
        eid = len(to)
        head[u].append(eid)
        to.append(v); cap.append(c); cost.append(w); rev.append(eid + 1)
        head[v].append(eid + 1)
        to.append(u); cap.append(0); cost.append(-w); rev.append(eid)

    for j in range(N - 1):
        add(S, j + 1, 1, 0)

    for j in range(N - 1):
        for i in range(j + 1, N):
            # 이익 = a[i]^a[j] - h[i], cost는 음수로
            add(j + 1, i + N + 1, 1, h[i] - (a[i] ^ a[j]))

    for i in range(N):
        c = l[i] if i == N - 1 else l[i] - 1
        add(i + N + 1, T, c, 0)

    # SPFA로 N-1번 augment
    INF = 10 ** 18
    total_cost = 0

    for _ in range(N - 1):
        dist = [INF] * V
        dist[S] = 0
        in_q = [False] * V
        pv = [-1] * V
        pe = [-1] * V
        q = deque([S])
        in_q[S] = True

        while q:
            u = q.popleft()
            in_q[u] = False
            du = dist[u]
            for eid in head[u]:
                if cap[eid] > 0:
                    nd = du + cost[eid]
                    v = to[eid]
                    if nd < dist[v]:
                        dist[v] = nd
                        pv[v] = u
                        pe[v] = eid
                        if not in_q[v]:
                            q.append(v)
                            in_q[v] = True

        v = T
        while v != S:
            eid = pe[v]
            cap[eid] -= 1
            cap[rev[eid]] += 1
            v = pv[v]

        total_cost += dist[T]

    # 각 비우승자의 패배 피로 합산
    h_losers = sum(h[j] for j in range(N - 1))
    print(-total_cost - h_losers)

solve()