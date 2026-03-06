import sys

# N 입력 받기
N = int(sys.stdin.readline())

for i in range(1, N + 1):
    # 공백 출력 + 별 출력
    print(" " * (N - i) + "*" * (2 * i - 1))