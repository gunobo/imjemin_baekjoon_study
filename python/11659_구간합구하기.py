import sys

def solve():
    # 입력 속도 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 수의 개수
    m = int(input_data[1]) # 합을 구해야 하는 횟수
    
    # 원본 수 리스트
    numbers = list(map(int, input_data[2:2+n]))
    
    # 누적 합 배열 생성 (인덱스 편의를 위해 n+1 크기로 설정)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + numbers[i]
    
    # 질의 처리
    results = []
    current_idx = 2 + n
    for _ in range(m):
        i = int(input_data[current_idx])
        j = int(input_data[current_idx + 1])
        # 구간 합 공식 적용: S[j] - S[i-1]
        results.append(str(prefix_sum[j] - prefix_sum[i-1]))
        current_idx += 2
        
    # 결과 출력
    print('\n'.join(results))

if __name__ == "__main__":
    solve()