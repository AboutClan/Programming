from collections import deque
import sys

input = sys.stdin.readline

cnt = int(input())
for _ in range(cnt):
    stack = deque()
    is_vps = True
    _list = list(map(str, input().strip()))
    for i in _list:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                a = stack.pop()
                if a == ")":
                    is_vps = False
                    break
            else:
                is_vps = False
                break
    print("YES" if (is_vps and not stack) else "NO")
