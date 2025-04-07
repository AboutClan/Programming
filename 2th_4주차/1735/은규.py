import sys

input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a3 = (a1 * b2) + (a2 * b1)
b3 = b1 * b2

c = gcd(a3, b3)

a3 = a3 // c
b3 = b3 // c

print(str(a3) + ' ' + str(b3))
