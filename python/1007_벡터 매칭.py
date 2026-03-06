import sys
import math
from itertools import combinations

input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = []
        total_x, total_y = 0, 0
        
        for _ in range(N):
            x, y = map(int, input().split())
            points.append((x, y))
            total_x += x
            total_y += y
            
        ans = float('inf')
        
        # N개 중 N/2개를 골라 '더하는 점'으로 설정
        for comb in combinations(points, N // 2):
            sum_x, sum_y = 0, 0
            for x, y in comb:
                sum_x += x
                sum_y += y
            
            # (더하는 점들의 합) - (빼는 점들의 합)
            # 빼는 점들의 합 = 전체 합 - 더하는 점들의 합
            current_vx = 2 * sum_x - total_x
            current_vy = 2 * sum_y - total_y
            
            length = math.sqrt(current_vx**2 + current_vy**2)
            ans = min(ans, length)
            
        print(f"{ans:.12f}")

solve()