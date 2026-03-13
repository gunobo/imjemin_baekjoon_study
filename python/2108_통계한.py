import sys
from collections import Counter

# 입력 속도 향상을 위한 설정
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    numbers = sorted([int(x) for x in data[1:]])

    # 1. 산술평균
    # 일반적인 반올림을 위해 sum/n 결과에 round 적용
    avg = round(sum(numbers) / n)
    print(avg)

    # 2. 중앙값
    print(numbers[n // 2])

    # 3. 최빈값
    counts = Counter(numbers).most_common()
    if len(counts) > 1:
        # 가장 많이 나타나는 빈도수 확인
        max_freq = counts[0][1]
        # 최빈값이 여러 개인지 확인 (정렬된 상태이므로 값 순서대로 들어있음)
        candidates = [val for val, freq in counts if freq == max_freq]
        candidates.sort() # 값 기준 정렬
        
        if len(candidates) > 1:
            print(candidates[1]) # 두 번째로 작은 값
        else:
            print(candidates[0])
    else:
        print(counts[0][0])

    # 4. 범위
    print(numbers[-1] - numbers[0])

solve()