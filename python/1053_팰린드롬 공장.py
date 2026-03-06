import sys

def solve():
    s_list = list(sys.stdin.readline().strip())
    n = len(s_list)

    def get_palindrome_cost(s):
        # dp[i][j]: s[i...j]를 팰린드롬으로 만드는 최소 비용
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if i+1 <= j-1 else 0
                else:
                    # 교체, 왼쪽 삭제/삽입, 오른쪽 삭제/삽입 중 최소 + 1
                    dp[i][j] = min(dp[i+1][j-1] if i+1 <= j-1 else 0,
                                   dp[i+1][j],
                                   dp[i][j-1]) + 1
        return dp[0][n-1]

    # 1. 4번 연산을 사용하지 않는 경우
    ans = get_palindrome_cost(s_list)

    # 2. 4번 연산(서로 다른 문자 교환)을 한 번 사용하는 경우
    for i in range(n):
        for j in range(i + 1, n):
            if s_list[i] != s_list[j]:
                # 교환 수행
                s_list[i], s_list[j] = s_list[j], s_list[i]
                # 교환 비용 1 + 나머지 팰린드롬화 비용
                ans = min(ans, get_palindrome_cost(s_list) + 1)
                # 원상 복구
                s_list[i], s_list[j] = s_list[j], s_list[i]

    print(ans)

solve()