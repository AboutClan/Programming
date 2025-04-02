a, b = map(int, input().split())

_list = [True for _ in range(b + 1)]
result = []
for i in range(2, b + 1):
    if _list[i]:
        for idx in range(i, b + 1, i):
            if idx <= b:
                _list[idx] = False
            else:
                break
        if i >= a:
            result.append(i)
for i in result:
    print(i)
