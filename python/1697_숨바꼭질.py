import sys
from collections import deque

def solve():
    # N: 수빈이 위치, K: 동생 위치
    n, k = map(int, sys.stdin.readline().split())
    
    # 최대 범위 설정 (0 ~ 100,000)
    MAX = 100001
    # 방문 여부 및 시간을 저장할 리스트 (-1은 미방문)
    time = [-1] * MAX
    
    queue = deque([n])
    time[n] = 0 # 시작 지점 시간은 0초
    
    while queue:
        curr = queue.popleft()
        
        # 동생을 찾으면 시간 출력 후 종료
        if curr == k:
            print(time[curr])
            return
        
        # 이동 가능한 3가지 경로 확인
        for next_pos in (curr - 1, curr + 1, curr * 2):
            if 0 <= next_pos < MAX: # 범위 내에 있고
                if time[next_pos] == -1: # 아직 방문하지 않았다면
                    time[next_pos] = time[curr] + 1
                    queue.append(next_pos)

solve()