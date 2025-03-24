from sys import stdin
N  = int(input())
c = set()
for i in range(N):
    name, status = stdin.readline().rstrip().split()
    if status == "enter":
        c.add(name)
    else:
        c.remove(name)

listc = list(c)
listc.sort(reverse=True)

for i in listc:
    print(i)
