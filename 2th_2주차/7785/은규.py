import sys

input = sys.stdin.readline

n = int(input())
people = set()

for _ in range(n):
    i, status = input().split()
    
    if i in people and status == 'leave':
        people.remove(i)
        
    if i not in people and status == 'enter':
        people.add(i)

for p in sorted(people, reverse=True):
    print(p)
