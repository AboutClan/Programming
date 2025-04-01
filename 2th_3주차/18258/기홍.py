from collections import deque
import sys

input = sys.stdin.readline

cnt = int(input())
q = deque()
for _ in range(cnt):
    _list = list(map(str, input().split()))
    cmd = _list[0]
    if cmd == "push":
        q.append(int(_list[1]))
    elif cmd == "pop":
        print(q.popleft() if q else -1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(1 if not q else 0)
    elif cmd == "front":
        print(q[0] if q else -1)
    elif cmd == "back":
        print(q[len(q) - 1] if q else -1)
