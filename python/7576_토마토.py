import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    m, n = map(int, input().split()) # m: 가로, n: 세로
    board = [list(map(int, input().split())) for _ in range(n)]
    
    queue = deque()
    
    # 1. 초기 익은 토마토 위치 찾기
    for r in range(n):
        for c in range(m):
            if board[r][c] == 1:
                queue.append((r, c))
    
    # 상하좌우 이동 방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 2. BFS 탐색
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 범위를 벗어나지 않고, 아직 익지 않은 토마토(0)인 경우
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
                board[nr][nc] = board[r][c] + 1 # 날짜 갱신 (누적)
                queue.append((nr, nc))
                
    # 3. 결과 확인
    max_days = 0
    for row in board:
        for val in row:
            if val == 0: # 익지 않은 토마토가 남아있다면
                print(-1)
                return
            max_days = max(max_days, val)
    
    # 저장될 때부터 다 익어있었다면 1-1=0이 출력됨
    print(max_days - 1)

solve()