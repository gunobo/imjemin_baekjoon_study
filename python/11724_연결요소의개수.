import sys

# DFS 재귀 한도 늘리기
sys.setrecursionlimit(2000)
input = sys.stdin.readline

def solve():
    # n: 정점의 개수, m: 간선의 개수
    n, m = map(int, input().split())
    
    # 인접 리스트 생성
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * (n + 1)
    count = 0

    def dfs(v):
        visited[v] = True
        for next_node in adj[v]:
            if not visited[next_node]:
                dfs(next_node)

    # 1번 정점부터 n번까지 확인
    for i in range(1, n + 1):
        if not visited[i]:
            # 방문하지 않은 정점을 만날 때마다 새로운 연결 요소 발견
            count += 1
            dfs(i)
            
    print(count)

solve()