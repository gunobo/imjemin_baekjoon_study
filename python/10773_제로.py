import sys

def solve():
    # 입력 속도 향상을 위해 readline 사용
    k = int(sys.stdin.readline())
    stack = []

    for _ in range(k):
        num = int(sys.stdin.readline())
        
        if num == 0:
            # 0이면 가장 최근의 수를 지움 (pop)
            stack.pop()
        else:
            # 0이 아니면 수를 추가 (push)
            stack.append(num)
            
    # 최종적으로 남은 수들의 합 출력
    print(sum(stack))

solve()