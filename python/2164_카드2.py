import sys
from collections import deque

def solve():
    # N 입력 받기
    input_data = sys.stdin.readline().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 1부터 N까지 카드를 큐에 담기
    cards = deque(range(1, n + 1))
    
    # 카드가 한 장 남을 때까지 반복
    while len(cards) > 1:
        # 1. 맨 앞의 카드를 버림
        cards.popleft()
        
        # 2. 그다음 맨 앞의 카드를 맨 뒤로 옮김
        if cards:
            cards.append(cards.popleft())
            
    # 마지막 남은 카드 출력
    print(cards[0])

solve()