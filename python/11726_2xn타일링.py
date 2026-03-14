import sys

def solve():
    # n 입력 받기
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)
    
    # n이 1일 경우 예외 처리
    if n == 1:
        print(1)
        return

    # dp 테이블 초기화
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    # 점화식: dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n + 1):
        # 문제에서 10,007로 나눈 나머지를 요구함
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
        
    print(dp[n])

solve()