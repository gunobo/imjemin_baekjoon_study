import sys
from collections import deque

def solve():
    # 테스트케이스 개수 입력
    t = int(sys.stdin.readline())

    for _ in range(t):
        # N: 문서의 개수, M: 궁금한 문서의 현재 위치
        n, m = map(int, sys.stdin.readline().split())
        # 중요도 입력받아 (중요도, 초기인덱스) 형태로 큐에 저장
        priorities = list(map(int, sys.stdin.readline().split()))
        queue = deque([(p, i) for i, p in enumerate(priorities)])
        
        count = 0 # 인쇄 횟수
        
        while queue:
            # 현재 가장 앞에 있는 문서
            current = queue.popleft()
            
            # 큐에 남아있는 문서들 중 현재보다 중요도가 높은 것이 있는지 확인
            if any(current[0] < doc[0] for doc in queue):
                # 더 중요한 게 있다면 맨 뒤로 보냄
                queue.append(current)
            else:
                # 현재 문서가 가장 중요하다면 인쇄
                count += 1
                # 만약 이 문서가 우리가 찾던 문서(M)라면 결과 출력
                if current[1] == m:
                    print(count)
                    break

solve()