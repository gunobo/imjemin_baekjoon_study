import sys
import heapq

def solve():
    # 입력 속도 최적화
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    operations = map(int, input[1:])
    
    heap = []
    
    results = []
    for x in operations:
        if x > 0:
            # 자연수라면 힙에 추가
            heapq.heappush(heap, x)
        else:
            # 0이라면 최솟값 출력 및 제거
            if not heap:
                results.append(0)
            else:
                results.append(heapq.heappop(heap))
    
    # 결과들을 한 번에 출력
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    solve()