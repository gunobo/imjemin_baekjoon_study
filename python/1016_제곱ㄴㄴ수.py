import sys
import math

# 입력 받기
min_val, max_val = map(int, sys.stdin.readline().split())

# min_val ~ max_val 사이의 숫자가 제곱ㄴㄴ수인지 체크 (True면 제곱ㄴㄴ수)
range_len = max_val - min_val + 1
is_square_free = [True] * range_len

# 2의 제곱(4)부터 sqrt(max)의 제곱까지 확인
for i in range(2, int(math.sqrt(max_val)) + 1):
    square = i * i
    
    # min_val보다 크거나 같은 square의 최소 배수 찾기
    start_val = (min_val // square) * square
    if start_val < min_val:
        start_val += square
    
    # 해당 제곱수의 배수들을 체에서 제외
    for j in range(start_val, max_val + 1, square):
        is_square_free[j - min_val] = False

print(is_square_free.count(True))