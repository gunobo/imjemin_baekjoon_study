import sys

# 일반적인 반올림(사사오입) 함수 정의
def my_round(val):
    return int(val + 0.5)

def solve():
    # 입력 속도 향상
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 1. 의견이 없는 경우 0 출력
    if n == 0:
        print(0)
        return
    
    # 의견 리스트 정렬
    opinions = sorted(map(int, input_data[1:]))
    
    # 2. 제외할 인원 계산 (15%)
    trim_num = my_round(n * 0.15)
    
    # 3. 절사평균 대상 데이터 추출
    # 슬라이싱을 이용해 앞뒤 trim_num만큼 제외
    if trim_num > 0:
        target_data = opinions[trim_num : n - trim_num]
    else:
        target_data = opinions
        
    # 4. 결과 계산 및 출력
    if not target_data:
        print(0)
    else:
        avg = sum(target_data) / len(target_data)
        print(my_round(avg))

solve()