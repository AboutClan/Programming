import sys

input = sys.stdin.readline
cnt = int(input())


def get_common_multiple(a, b):
    m = max([a, b])
    _list = []
    while m > 1:
        if not (a % m) and not (b % m):
            a = a // m
            b = b // m
            _list.append(m)
        else:
            m = m - 1
    result = a * b
    for i in _list:
        result = result * i
    return result


for _ in range(cnt):
    a, b = map(int, input().split())
    print(get_common_multiple(a, b))
