import sys

def solve():
    # 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    paper = []
    idx = 1
    for _ in range(n):
        paper.append(list(map(int, input_data[idx:idx+n])))
        idx += n

    white = 0 # 0의 개수
    blue = 0  # 1의 개수

    def check(r, c, size):
        nonlocal white, blue
        color = paper[r][c]
        
        for i in range(r, r + size):
            for j in range(c, c + size):
                if paper[i][j] != color:
                    # 색이 다르면 4등분하여 재귀 호출
                    new_size = size // 2
                    check(r, c, new_size)               # 1사분면
                    check(r, c + new_size, new_size)    # 2사분면
                    check(r + new_size, c, new_size)    # 3사분면
                    check(r + new_size, c + new_size, new_size) # 4사분면
                    return

        # 모든 칸의 색이 같을 경우
        if color == 0:
            white += 1
        else:
            blue += 1

    check(0, 0, n)
    print(white)
    print(blue)

solve()