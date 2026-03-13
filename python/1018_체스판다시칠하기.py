import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(n)]
    
    repair_counts = []

    # 1. 8x8로 자를 수 있는 모든 시작점 탐색
    for i in range(n - 7):
        for j in range(m - 7):
            white_start = 0 # 맨 왼쪽 위가 'W'인 경우를 만들기 위해 칠할 개수
            black_start = 0 # 맨 왼쪽 위가 'B'인 경우를 만들기 위해 칠할 개수
            
            # 2. 8x8 영역 검사
            for row in range(i, i + 8):
                for col in range(j, j + 8):
                    # 행+열 합이 짝수이면 시작점과 같은 색, 홀수이면 다른 색이어야 함
                    if (row + col) % 2 == 0:
                        if board[row][col] != 'W':
                            white_start += 1
                        if board[row][col] != 'B':
                            black_start += 1
                    else:
                        if board[row][col] != 'B':
                            white_start += 1
                        if board[row][col] != 'W':
                            black_start += 1
            
            repair_counts.append(white_start)
            repair_counts.append(black_start)

    # 3. 전체 중 최솟값 출력
    print(min(repair_counts))

solve()