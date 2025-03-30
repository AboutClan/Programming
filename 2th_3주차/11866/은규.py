import sys

input = sys.stdin.readline

n, k = map(int, input().split()) # 사람, 제거 번호

circle = [i for i in range(n)]
index = 0

print('<', end='')
while len(circle) != 0:
    index = (index + k - 1) % len(circle)
    
    if len(circle) != 1:
        print(circle.pop(index) + 1, end=', ')
    else:
        print(circle.pop(index) + 1, end='>')
