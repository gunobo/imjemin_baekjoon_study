import sys
from math import ceil
 
def input():
    return sys.stdin.readline().rstrip()
 
 
N,AC,AP,BC,BP = map(int,input().split())
 
if AP*BC < BP*AC:
    AC,AP,BC,BP = BC,BP,AC,AP
 
 
answer = float('inf')
 
for A_COUNT in range(BC):
    B_COUNT = ceil((N-A_COUNT*AC)/BC)
    isover = False
    if B_COUNT<0:
        B_COUNT = 0
        isover = True
    answer = min(answer, A_COUNT*AP + B_COUNT*BP)
    if isover:
        break
 
print(answer)