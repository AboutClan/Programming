n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
_dict = {}
for i in range(n):
    _dict[n_list[i]] = 0

for j in range(m):
    if m_list[j] in _dict:
        print(1, end=' ')
    else:
        print(0, end=' ')