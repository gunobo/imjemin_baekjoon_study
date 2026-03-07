import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

min_val = min(numbers)
max_val = max(numbers)

print(min_val, max_val)