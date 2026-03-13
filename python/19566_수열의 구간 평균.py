import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()
 
N,M = map(int,input().split())
 
arr = list(map(int,input().split()))
 
 
prefix_sum = [0] + arr[:]
result = 0
num_dict = defaultdict(int)
for i in range(1,N+1):
    prefix_sum[i] += prefix_sum[i-1]
    calc = prefix_sum[i] - M*i
 
    result += num_dict[calc]
    num_dict[calc] += 1
 
 
print(result+num_dict[0])