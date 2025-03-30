from collections import deque
import sys

def push(x):
    queue.append(x)

def pop():
    if len(queue) > 0:
        return queue.popleft()
    else:
        return '-1'
    
def size():
    return len(queue)

def empty():
    if len(queue) > 0:
        return '0'
    else:
        return '1'
    
def front():
    if len(queue) > 0:
        return queue[0]
    else:
        return '-1'
    
def back():
    if len(queue) > 0:
        return queue[-1]
    else:
        return '-1'

queue = deque()

n = int(input())

for _ in range(n):
    x = sys.stdin.readline()
    
    if 'push' in x:
        push(x.split()[1])
    elif 'pop' in x:
        print(pop())
    elif 'size' in x:
        print(size())
    elif 'empty' in x:
        print(empty())
    elif 'front' in x:
        print(front())
    else:
        print(back())
