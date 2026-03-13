import sys
from collections import Counter

def solve():
    # 입력 속도 향상을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # 상근이가 가진 카드의 개수 N
    n = int(input_data[0])
    # 상근이의 카드 리스트 (인덱스 1부터 N까지)
    cards = input_data[1:n+1]
    
    # 1. 각 카드의 개수를 미리 세어 딕셔너리 형태로 저장
    card_counts = Counter(cards)
    
    # 구해야 할 숫자의 개수 M
    m = int(input_data[n+1])
    # 구해야 할 숫자 리스트
    targets = input_data[n+2:]
    
    # 2. 결과 리스트 생성
    result = []
    for target in targets:
        # 딕셔너리에서 개수 조회 (없으면 0)
        result.append(str(card_counts.get(target, 0)))
    
    # 3. 공백으로 구분하여 출력
    print(" ".join(result))

solve()