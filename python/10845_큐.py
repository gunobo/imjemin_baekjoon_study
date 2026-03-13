import sys
from collections import deque

def solve():
    # 명령의 개수 N 입력
    n = int(sys.stdin.readline())
    queue = deque()

    for _ in range(n):
        # 명령어를 읽어와 공백으로 분리
        command = sys.stdin.readline().split()
        
        cmd_type = command[0]

        if cmd_type == 'push':
            queue.append(command[1])
            
        elif cmd_type == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
                
        elif cmd_type == 'size':
            print(len(queue))
            
        elif cmd_type == 'empty':
            print(0 if queue else 1)
            
        elif cmd_type == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
                
        elif cmd_type == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)

solve()