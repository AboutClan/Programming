import sys
N = int(sys.stdin.readline().strip())
num = 666
cnt = 1
while True:
    if '666' in str(num) and cnt == N:
        print(num)
        break

    if '666' in str(num):
        cnt += 1
        
    num += 1