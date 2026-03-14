import sys

# DFS 재귀 한도 설정 (N이 최대 100이므로 10000 정도면 충분합니다)
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]

    # 상하좌우 이동 방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(r, c, color, grid, visited):
        visited[r][c] = True
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 범위 내에 있고, 아직 방문하지 않았으며, 색상이 같은 경우 탐색 계속
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and grid[nr][nc] == color:
                    dfs(nr, nc, color, grid, visited)

    def count_areas(grid):
        visited = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    dfs(i, j, grid[i][j], grid, visited)
                    count += 1
        return count

    # 1. 일반인이 보는 구역 수 계산
    normal_count = count_areas(board)

    # 2. 적록색약용 보드로 변환 (G를 R로 바꿈)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'G':
                board[i][j] = 'R'
    
    # 3. 적록색약이 보는 구역 수 계산
    blind_count = count_areas(board)

    print(normal_count, blind_count)

solve()