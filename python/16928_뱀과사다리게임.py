import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # 사다리와 뱀 정보를 하나의 딕셔너리에 통합
    teleport = {}
    for _ in range(n + m):
        u, v = map(int, input().split())
        teleport[u] = v
    
    # 방문 체크 및 큐 초기화
    visited = [False] * 101
    queue = deque([(1, 0)]) # (현재 위치, 주사위 횟수)
    visited[1] = True
    
    while queue:
        curr, count = queue.popleft()
        
        # 100번 칸에 도착하면 횟수 반환
        if curr == 100:
            print(count)
            return
        
        # 주사위 1~6 굴리기
        for i in range(1, 7):
            next_pos = curr + i
            
            if next_pos <= 100:
                # 사다리나 뱀이 있는 칸이라면 이동
                if next_pos in teleport:
                    next_pos = teleport[next_pos]
                
                # 방문하지 않은 칸이라면 큐에 추가
                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append((next_pos, count + 1))

solve()