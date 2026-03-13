import sys
from collections import deque
 
def input():
    return sys.stdin.readline().rstrip()
A = list(input())
 
B = list(input())
N = len(A)
 
A.sort()
B.sort()
A = deque(A[:(N+1)//2])
B = deque(B[N-N//2:N])
answer = ['?']*N
left = 0
right = N-1
 
for idx in range(N):
    if idx%2:
        if A and A[0] >= B[-1]:
            answer[right] = B.popleft()
            right -= 1
        else:
            answer[left] = B.pop()
            left += 1
    else:
        if B and B[-1] <= A[0]:
            answer[right] = A.pop()
            right -= 1
        else:
            answer[left] = A.popleft()
            left += 1
 
 
print(''.join(answer))