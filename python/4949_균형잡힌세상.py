import sys

def solve():
    while True:
        # 한 줄씩 읽기 (온점 포함)
        line = sys.stdin.readline().rstrip('\n')
        
        # 종료 조건: 온점 하나만 들어온 경우
        if line == ".":
            break
            
        stack = []
        is_balanced = True
        
        for char in line:
            # 1. 왼쪽 괄호는 스택에 추가
            if char == '(' or char == '[':
                stack.append(char)
            
            # 2. 소괄호 닫기
            elif char == ')':
                if not stack or stack[-1] != '(':
                    is_balanced = False
                    break
                stack.pop()
            
            # 3. 대괄호 닫기
            elif char == ']':
                if not stack or stack[-1] != '[':
                    is_balanced = False
                    break
                stack.pop()
        
        # 모든 검사 후 스택이 비어있어야 완벽한 균형
        if is_balanced and not stack:
            print("yes")
        else:
            print("no")

solve()