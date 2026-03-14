import sys

def solve():
    # n: 나무의 수, m: 필요한 나무 길이
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    trees = list(map(int, input_data[2:]))

    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(trees)
    
    result = 0
    while start <= end:
        mid = (start + end) // 2 # 절단기 높이 H
        
        # 잘린 나무들의 합 계산
        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid
        
        # 합이 m보다 크거나 같으면, 높이를 더 높여본다 (최댓값 찾기)
        if total >= m:
            result = mid
            start = mid + 1
        # 합이 m보다 작으면, 나무를 더 많이 잘라야 하므로 높이를 낮춘다
        else:
            end = mid - 1
            
    print(result)

solve()