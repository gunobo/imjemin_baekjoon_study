import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split()) # n: 세로, m: 가로
    
    board = []
    dist = [[-1] * m for _ in range(n)] # 거리를 저장할 배열 (-1로 초기화)
    queue = deque()

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] == 2: # 목표 지점 발견
                queue.append((i, j))
                dist[i][j] = 0
            elif row[j] == 0: # 갈 수 없는 땅은 거리를 0으로 고정
                dist[i][j] = 0
        board.append(row)

    # 상하좌우 이동 방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # BFS 탐색
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 지도 범위 내에 있고, 아직 방문하지 않은(-1) 갈 수 있는 땅(1)인 경우
            if 0 <= nr < n and 0 <= nc < m:
                if dist[nr][nc] == -1 and board[nr][nc] == 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    # 결과 출력
    for row in dist:
        print(*(row))

solve()