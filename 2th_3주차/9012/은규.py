import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    data = list(input().strip())
    stack = []
    result = False

    for i in data:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                result = True
                break
            stack.pop()

    if len(stack) != 0 or result:
        print("NO")
    else:
        print("YES")
