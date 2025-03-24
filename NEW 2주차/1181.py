import sys
N = int(sys.stdin.readline())
list1 = []
for i in range(N):
    list1.append(sys.stdin.readline().strip())
setlist = set(list1)
list1 = list(setlist)
list1.sort()
list1.sort(key = len)

for i in list1:
    print(i)