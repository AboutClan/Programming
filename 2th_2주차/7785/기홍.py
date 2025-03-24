import sys

input = sys.stdin.readline

cnt = int(input())
_list = {}
for _ in range(cnt):
    name, status = map(str, input().split())
    if status == "enter":
        _list[name] = status
    elif status == "leave":
        _list.pop(
            name, None
        )  # 키 값이 존재하지 않는 경우, 에러가 발생하기 때문에 None을 넣어줌.

_list = dict(sorted(_list.items(), key=lambda item: item[0], reverse=True))

for name in _list:
    print(name)
