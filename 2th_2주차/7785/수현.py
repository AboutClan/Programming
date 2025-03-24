import sys

n = int(sys.stdin.readline().strip())
exist = set()

for _ in range(n):
    log = sys.stdin.readline().strip()
    name, status = log.split()
    
    if status == "enter":
        exist.add(name)
    elif status == "leave":
        exist.remove(name)

for p in sorted(exist, reverse=True):
    print(p)