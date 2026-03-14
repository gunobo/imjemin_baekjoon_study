import sys
from collections import deque

def solve():
    input_data = sys.stdin.readline
    t = int(input_data())

    for _ in range(t):
        p = input_data().strip() # 수행할 함수
        n = int(input_data())    # 배열의 원소 개수
        # [1,2,3,4] 형태를 리스트로 변환
        arr_raw = input_data().strip()[1:-1]
        
        if arr_raw == "":
            queue = deque()
        else:
            queue = deque(arr_raw.split(','))
        
        is_reversed = False # 현재 뒤집힌 상태인지 확인하는 플래그
        is_error = False

        for cmd in p:
            if cmd == 'R':
                is_reversed = not is_reversed
            elif cmd == 'D':
                if not queue:
                    is_error = True
                    break
                # 뒤집힌 상태에 따라 앞 또는 뒤에서 제거
                if is_reversed:
                    queue.pop()
                else:
                    queue.popleft()

        if is_error:
            print("error")
        else:
            # 출력할 때 현재 상태가 역방향이면 실제로 뒤집어서 출력
            if is_reversed:
                queue.reverse()
            print("[" + ",".join(queue) + "]")

solve()