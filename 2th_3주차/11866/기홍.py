import sys

input = sys.stdin.readline
a, b = map(int, input().split())
q = []
for i in range(1, a + 1):
    q.append(i)
i = 1
result = []
idx = b - 1
while q:
    if idx < len(q):
        result.append(q.pop(idx))
    else:
        result.append(q.pop(idx))
    # print(f"idx = {idx}")
    try:
        idx = idx + b - 1 if q and (idx + (b - 1)) < len(q) else (idx + b - 1) % len(q)
    except:
        break
print("<", end="")
print(*result, sep=", ", end=">")
