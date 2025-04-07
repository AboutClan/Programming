import sys

input = sys.stdin.readline

t = int(input())

data = []
for _ in range(t):
    data.append(list(map(int, input().split())))

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return int((a * b) / gcd(a, b))

for a, b in data:
    if a < b:
        print(lcm(a, b))
    else:
        print(lcm(b, a))
