from collections import deque
import sys

input = sys.stdin.readline
cnt = int(input())

stack = deque()
for _ in range(cnt):
    _list = list(map(int, input().split()))
    a = _list[0]
    if a == 1:
        b = _list[1]
        stack.append(b)
    elif a == 2:
        print(stack.pop() if stack else -1)
    elif a == 3:
        print(len(stack))
    elif a == 4:
        print(1 if not stack else 0)
    elif a == 5:
        print(stack[len(stack) - 1] if stack else -1)
