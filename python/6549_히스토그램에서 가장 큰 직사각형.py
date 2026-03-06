import sys
input = sys.stdin.readline

def solve(heights):
    stack = []  # (index, height)
    max_area = 0
    
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))
    
    return max_area

for line in sys.stdin:
    nums = list(map(int, line.split()))
    if nums[0] == 0:
        break
    print(solve(nums[1:]))