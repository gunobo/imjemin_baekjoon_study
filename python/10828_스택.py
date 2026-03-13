import sys

def solve():
    # 명령의 개수 N 입력
    n = int(sys.stdin.readline())
    stack = []

    for _ in range(n):
        # 명령어를 입력받아 공백으로 분리
        command = sys.stdin.readline().split()
        
        cmd_type = command[0]

        if cmd_type == 'push':
            stack.append(command[1])
            
        elif cmd_type == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
                
        elif cmd_type == 'size':
            print(len(stack))
            
        elif cmd_type == 'empty':
            print(0 if stack else 1)
            
        elif cmd_type == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)

solve()