import sys

def solve():
    n, r, c = map(int, sys.stdin.readline().split())
    
    ans = 0
    while n != 0:
        n -= 1
        half = 2 ** n # 사분면 한 변의 길이
        
        # 1사분면 (왼쪽 위)
        if r < half and c < half:
            ans += 0
        
        # 2사분면 (오른쪽 위)
        elif r < half and c >= half:
            ans += half * half
            c -= half
            
        # 3사분면 (왼쪽 아래)
        elif r >= half and c < half:
            ans += (half * half) * 2
            r -= half
            
        # 4사분면 (오른쪽 아래)
        else:
            ans += (half * half) * 3
            r -= half
            c -= half
            
    print(ans)

solve()