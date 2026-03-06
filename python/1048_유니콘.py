import sys

# 입력을 빠르게 읽기 위한 설정
input = sys.stdin.read

def solve():
    # 데이터를 한 번에 읽어와 공백 단위로 분리
    data = input().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1 # L 또는 K (단어의 길이와 무관하게 입력되는 값)
    
    word = data[idx]; idx += 1
    board = data[idx:idx+N]; idx += N
    
    W = len(word)
    MOD = 1_000_000_007
    
    # dp[i][j]: 현재 위치 (i, j)에서 word[k]까지 완성하는 경우의 수
    dp = [[0] * M for _ in range(N)]
    
    # 1. 초기화: 첫 번째 글자 위치 찾기
    char0 = word[0]
    for r in range(N):
        row_str = board[r]
        dpr = dp[r]
        for c in range(M):
            if row_str[c] == char0:
                dpr[c] = 1
                
    # 단어가 한 글자인 경우 예외 처리
    if W == 1:
        print(sum(sum(row) for row in dp) % MOD)
        return

    # 2. DP 전이: 두 번째 글자부터 끝까지
    for k in range(1, W):
        target_char = word[k]
        
        # 2D Prefix Sum (P) 생성
        # P[r][c]는 board의 (0,0)부터 (r-1, c-1)까지의 dp 합
        P = [[0] * (M + 1) for _ in range(N + 1)]
        for r in range(N):
            row_sum = 0
            Pr = P[r]
            Pr1 = P[r+1]
            dpr = dp[r]
            for c in range(M):
                row_sum = (row_sum + dpr[c]) % MOD
                Pr1[c+1] = (Pr[c+1] + row_sum) % MOD
        
        new_dp = [[0] * M for _ in range(N)]
        total_sum = P[N][M]
        
        for r in range(N):
            row_str = board[r]
            new_dpr = new_dp[r]
            
            # r-1 ~ r+1 범위를 제외하기 위한 행 인덱스 계산
            r_start, r_end = max(0, r - 1), min(N - 1, r + 1)
            
            for c in range(M):
                if row_str[c] != target_char:
                    continue
                
                # c-1 ~ c+1 범위를 제외하기 위한 열 인덱스 계산
                c_start, c_end = max(0, c - 1), min(M - 1, c + 1)
                
                # 구간 합 공식: P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
                # (r-1 ~ r+1, c-1 ~ c+1) 영역의 합을 구함
                near_sum = (P[r_end+1][c_end+1] - P[r_start][c_end+1] - 
                            P[r_end+1][c_start] + P[r_start][c_start]) % MOD
                
                # 전체 합에서 인접 영역을 제외하여 '멀리 떨어진' 칸들의 합 계산
                new_dpr[c] = (total_sum - near_sum) % MOD
        
        dp = new_dp

    # 3. 최종 결과 출력
    final_ans = sum(sum(row) for row in dp) % MOD
    print(final_ans)

if __name__ == "__main__":
    solve()