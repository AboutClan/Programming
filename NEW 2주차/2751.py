import sys
n = int(input())
list1 = []
for _ in range(n):
    list1.append(int(sys.stdin.readline()))

list1.sort()
for i in list1:
    print(i)