t = int(input())

for _ in range(t):
    data = input().split()
    r = int(data[0])  # 첫 번째 값은 반복 횟수
    s = data[1]       # 두 번째 값은 문자열
    
    result = ""
    for char in s:
        result += char * r
    
    print(result)