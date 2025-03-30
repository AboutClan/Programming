import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    cmd = input().rstrip()
    
    if len(cmd) != 1:
        stack.append(int(cmd[2:]))
        
    elif cmd == '2':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
            
    elif cmd == '3':
        print(len(stack))
        
    elif cmd == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif cmd == '5':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
        
