import sys

def solve():
    # 입력 속도 향상을 위한 설정
    input = sys.stdin.read().split()
    if not input:
        return 
    
    N = int(input[0])
    meetings = []
    
    # 데이터 읽기 (시작 시간, 종료 시간)
    for i in range(N):
        start = int(input[2*i + 1])
        end = int(input[2*i + 2])
        meetings.append((start, end))
        
    # 1. 끝나는 시간 기준 오름차순, 2. 시작 시간 기준 오름차순 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    count = 0
    last_end_time = 0
    
    for start, end in meetings:
        # 현재 회의 시작 시간이 이전 회의 종료 시간 이후라면 선택
        if start >= last_end_time:
            count += 1
            last_end_time = end
            
    print(count)

if __name__ == "__main__":
    solve()