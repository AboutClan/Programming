import sys
import math

input = sys.stdin.readline

m, n = map(int, input().split())

decimal = set(i for i in range(m, n + 1) if i != 1)

for e in range(2, int(math.sqrt(n) + 1)):
    for d in range(e * e, n + 1, e):
        decimal.discard(d)
            
for d in decimal:
    print(d)
