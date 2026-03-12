import sys

def count_inversions(n, arr):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        arr = list(map(int, input_data[idx : idx + n]))
        idx += n
        
        if count_inversions(n, arr) % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
            
    print("\n".join(results))

if __name__ == "__main__":
    solve()