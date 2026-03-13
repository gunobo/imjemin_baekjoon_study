import sys

def solve():
    # 설탕의 무게 N 입력
    n = int(sys.stdin.readline())
    
    bags = 0
    while n >= 0:
        # 5로 나누어떨어지면 바로 계산 종료
        if n % 5 == 0:
            bags += (n // 5)
            print(bags)
            return
        
        # 5로 안 나누어지면 3kg 봉지 하나 추가 후 다시 검사
        n -= 3
        bags += 1
    
    # 반복문이 정상적으로 종료되지 않고 n이 음수가 되면 불가능한 경우
    print(-1)

solve()