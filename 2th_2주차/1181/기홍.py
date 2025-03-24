import sys

input = sys.stdin.readline

repeat = int(input())

_list = []

for _ in range(repeat):
    a = input().strip()
    if a in _list:
        continue
    _list.append(a)

_list.sort(key=lambda x: (len(x), x))

for i in _list:
    print(i, end="\n")
