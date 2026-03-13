import sys

# 단어 S를 입력받음
s = sys.stdin.readline().strip()

# 알파벳 소문자 리스트 (a-z)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 각 알파벳이 단어 S의 어디에 있는지 확인
for char in alphabet:
    # find() 메서드는 찾는 문자가 있으면 첫 번째 인덱스를, 없으면 -1을 반환함
    print(s.find(char), end=' ')