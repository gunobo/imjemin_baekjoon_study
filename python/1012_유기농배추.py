import sys

# DFS 재귀 한도 설정 (M, N이 최대 50이므로 충분히 설정)
sys.setrecursionlimit(3000)
input = sys.stdin.readline

def solve():
    t = int(input()) # 테스트 케이스 개수
    
    for _ in range(t):
        m, n, k = map(int, input().split())
        # 배추밭 초기화 (n행 m열)
        field = [[0] * m for _ in range(n)]
        
        # 배추 위치 입력
        for _ in range(k):
            x, y = map(int, input().split())
            field[y][x] = 1 # 가로(x)가 열, 세로(y)가 행
            
        visited = [[False] * m for _ in range(n)]
        count = 0

        # 상하좌우 이동 방향
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r, c):
            visited[r][c] = True
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if field[nr][nc] == 1 and not visited[nr][nc]:
                        dfs(nr, nc)

        # 모든 칸을 순회하며 군집 찾기
        for i in range(n):
            for j in range(m):
                if field[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        
        print(count)

solve()