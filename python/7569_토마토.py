import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    # m: 가로, n: 세로, h: 높이
    m, n, h = map(int, input().split())
    
    # 3차원 창고 데이터 입력
    board = []
    queue = deque()
    
    for i in range(h):
        layer = []
        for j in range(n):
            row = list(map(int, input().split()))
            for k in range(m):
                # 익은 토마토인 경우 큐에 좌표 삽입 (높이, 세로, 가로)
                if row[k] == 1:
                    queue.append((i, j, k))
            layer.append(row)
        board.append(layer)

    # 6방향 이동 (위, 아래, 앞, 뒤, 좌, 우)
    dx = [1, -1, 0, 0, 0, 0] # h
    dy = [0, 0, 1, -1, 0, 0] # n
    dz = [0, 0, 0, 0, 1, -1] # m

    # BFS 시작
    while queue:
        curr_h, curr_n, curr_m = queue.popleft()
        
        for i in range(6):
            nh, nn, nm = curr_h + dx[i], curr_n + dy[i], curr_m + dz[i]
            
            # 창고 범위 내에 있고 익지 않은 토마토(0)인 경우
            if 0 <= nh < h and 0 <= nn < n and 0 <= nm < m:
                if board[nh][nn][nm] == 0:
                    board[nh][nn][nm] = board[curr_h][curr_n][curr_m] + 1
                    queue.append((nh, nn, nm))

    # 결과 계산
    ans = 0
    for layer in board:
        for row in layer:
            for tomato in row:
                if tomato == 0:
                    print(-1)
                    return
                ans = max(ans, tomato)
    
    # 시작값이 1이었으므로 1을 빼줌
    print(ans - 1)

solve()