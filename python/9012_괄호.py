import sys

def solve():
    # 테스트 케이스의 수 T 입력
    t = int(sys.stdin.readline())

    for _ in range(t):
        ps = sys.stdin.readline().strip()
        stack = []
        is_vps = True

        for char in ps:
            if char == '(':
                stack.append(char)
            else: # char == ')'
                if not stack:
                    # 스택이 비어있는데 ')'가 나오면 짝이 안 맞음
                    is_vps = False
                    break
                stack.pop()
        
        # 문자열을 다 돌았는데 스택에 '('가 남아있어도 안 됨
        if is_vps and not stack:
            print("YES")
        else:
            print("NO")

solve()