import sys
from collections import deque

def solve():
    # N(사람 수)과 K(제거할 간격) 입력
    n, k = map(int, sys.stdin.readline().split())
    
    # 1부터 N까지 담긴 큐 생성
    queue = deque(range(1, n + 1))
    result = []

    while queue:
        # K-1번만큼 앞에서 꺼내 뒤로 보냄 (순환)
        for _ in range(k - 1):
            queue.append(queue.popleft())
        
        # K번째 사람을 제거하여 결과에 추가
        result.append(str(queue.popleft()))

    # 출력 형식 맞추기: <val1, val2, ...>
    print("<" + ", ".join(result) + ">")

solve()