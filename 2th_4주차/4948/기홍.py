MAX = 123456 * 2
_list = [1 for _ in range(MAX + 1)]
_list[0] = _list[1] = 0

cnt = 0
for idx in range(2, MAX):
    if _list[idx] == 1:
        cnt = cnt + 1
        _list[idx] = cnt
        for idx_2 in range(idx * 2, MAX, idx):
            _list[idx_2] = 0


def find_decimal(num):
    return max(_list[: num * 2 + 1]) - max(_list[: num + 1])


while 1:
    n = int(input())
    if not n:
        break
    print(find_decimal(n))
