# input으로 읽고 -> split으로 나누고 -> int로 바꿔서 -> 제곱한 뒤 -> sum으로 다 더함
print(sum(int(x)**2 for x in input().split()) % 10)