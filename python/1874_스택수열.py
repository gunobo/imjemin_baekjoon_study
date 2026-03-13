import sys

def solve():
    n = int(sys.stdin.readline())
    stack = []
    result = []
    count = 1
    possible = True

    for _ in range(n):
        target = int(sys.stdin.readline())
        
        # target까지 오름차순으로 push
        while count <= target:
            stack.append(count)
            result.append('+')
            count += 1
        
        # 스택의 가장 위 숫자가 target이면 pop
        if stack[-1] == target:
            stack.pop()
            result.append('-')
        else:
            # target을 만들 수 없는 경우
            possible = False
            break

    if possible:
        print('\n'.join(result))
    else:
        print("NO")

solve()