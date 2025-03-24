import sys

input = sys.stdin.readline

repeat = int(input())
_list = []
for _ in range(repeat):
    _list.append(int(input()))

_list.sort()

for a in _list:
    print(a, end="\n")
