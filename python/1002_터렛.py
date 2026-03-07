import sys

# 입력 속도를 위해 sys.stdin.read 사용
input = sys.stdin.read().split()

def solve():
    if not input:
        return
        
    T = int(input[0])
    idx = 1
    
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input[idx:idx+6])
        idx += 6
        
        # 두 터렛 사이 거리의 제곱 (x^2 + y^2)
        d_sq = (x2 - x1)**2 + (y2 - y1)**2
        
        # 반지름 합의 제곱과 차의 제곱
        sum_r_sq = (r1 + r2)**2
        diff_r_sq = (r1 - r2)**2
        
        # 1. 두 원이 완전히 일치하는 경우 (중심이 같고 반지름도 같음)
        if d_sq == 0 and r1 == r2:
            print(-1)
        # 2. 한 점에서 만나는 경우 (외접 또는 내접)
        elif d_sq == sum_r_sq or d_sq == diff_r_sq:
            print(1)
        # 3. 두 점에서 만나는 경우
        elif diff_r_sq < d_sq < sum_r_sq:
            print(2)
        # 4. 만나지 않는 경우
        else:
            print(0)

if __name__ == "__main__":
    solve()