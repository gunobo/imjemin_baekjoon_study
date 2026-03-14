import sys

def solve():
    # 입력 속도 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 원본 좌표 리스트
    x_list = list(map(int, input_data[1:]))
    
    # 1. 중복 제거 후 정렬
    sorted_unique_x = sorted(list(set(x_list)))
    
    # 2. 각 숫자에 대해 인덱스(압축된 좌표) 매핑
    # 예: {숫자: 순위} 형태의 딕셔너리 생성
    dic = {val: i for i, val in enumerate(sorted_unique_x)}
    
    # 3. 원본 좌표를 순회하며 딕셔너리에서 변환된 값 추출
    result = []
    for x in x_list:
        result.append(str(dic[x]))
        
    # 공백으로 구분하여 한 번에 출력
    print(" ".join(result))

solve()