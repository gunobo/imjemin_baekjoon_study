import sys

def solve():
    # 입력 받기
    m, n = map(int, sys.stdin.readline().split())

    # 0부터 n까지의 소수 판별 리스트 (True는 소수, False는 아님)
    # 처음에는 모두 소수로 가정
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]: # i가 소수라면
            # i의 배수들을 모두 False로 변경 (i*i부터 시작해도 됨)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # m 이상 n 이하의 소수 출력
    for i in range(m, n + 1):
        if is_prime[i]:
            print(i)

solve()