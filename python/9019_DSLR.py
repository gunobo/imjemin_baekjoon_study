import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        
        # visited 배열: 해당 숫자를 방문했는지 체크
        visited = [False] * 10000
        # 큐: (현재 숫자, 현재까지의 명령어 문자열)
        queue = deque([(a, "")])
        visited[a] = True

        while queue:
            curr, path = queue.popleft()

            if curr == b:
                print(path)
                break

            # 1. D 연산
            next_d = (curr * 2) % 10000
            if not visited[next_d]:
                visited[next_d] = True
                queue.append((next_d, path + "D"))

            # 2. S 연산
            next_s = (curr - 1) % 10000
            if not visited[next_s]:
                visited[next_s] = True
                queue.append((next_s, path + "S"))

            # 3. L 연산: d1 d2 d3 d4 -> d2 d3 d4 d1
            next_l = (curr % 1000) * 10 + (curr // 1000)
            if not visited[next_l]:
                visited[next_l] = True
                queue.append((next_l, path + "L"))

            # 4. R 연산: d1 d2 d3 d4 -> d4 d1 d2 d3
            next_r = (curr % 10) * 1000 + (curr // 10)
            if not visited[next_r]:
                visited[next_r] = True
                queue.append((next_r, path + "R"))

solve()