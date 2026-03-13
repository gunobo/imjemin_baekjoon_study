import sys

# 입력 설정
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 테트로미노가 가질 수 있는 최댓값 (가지치기용)
max_val = max(map(max, board))
ans = 0

# 상하좌우 이동 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, depth, total):
    global ans
    # 가지치기: 현재 합 + 남은 칸 * 보드 최댓값이 현재 정답보다 작으면 중단
    if total + max_val * (4 - depth) <= ans:
        return
    
    # 4칸을 모두 골랐을 때
    if depth == 4:
        ans = max(ans, total)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            # 'ㅗ' 모양 처리를 위한 로직
            if depth == 2:
                visited[nr][nc] = True
                dfs(r, c, depth + 1, total + board[nr][nc])
                visited[nr][nc] = False
            
            visited[nr][nc] = True
            dfs(nr, nc, depth + 1, total + board[nr][nc])
            visited[nr][nc] = False

# 모든 칸을 시작점으로 탐색
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)