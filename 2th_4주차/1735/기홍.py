# 해당 문제는 어떻게 풀어야 할지 전혀 아이디어가 안 떠오름. => 분명 풀었던 건데 까먹었다....
a, b = map(int, input().split())
c, d = map(int, input().split())


# 유클리드 호제법 사용
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


parent = b * d
child = a * d + b * c
_gcd = gcd(parent, child)
parent = parent // _gcd
child = child // _gcd
print(child, parent)
