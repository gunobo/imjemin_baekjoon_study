import sys

while True:
    # 세 변의 길이를 입력받아 리스트로 저장
    sides = list(map(int, sys.stdin.readline().split()))
    
    # 입력의 마지막 줄인 0 0 0 인 경우 종료
    if sum(sides) == 0:
        break
    
    # 가장 긴 변을 찾기 위해 오름차순 정렬
    sides.sort()
    
    # 피타고라스 정리 적용: a^2 + b^2 == c^2
    if (sides[0]**2 + sides[1]**2) == sides[2]**2:
        print("right")
    else:
        print("wrong")