import sys

input = sys.stdin.readline

n = int(input())
sanguen = set(map(int, input().split()))

m = int(input())
numbers = set(map(int, input().split()))

for n in numbers:
    if n in sanguen:
        print(1, end=' ')
    else:
        print(0, end=' ')
