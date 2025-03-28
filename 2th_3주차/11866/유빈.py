# 11866 : 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def answer(self):
        n, k = map(int, input().split())
        Q = deque(map(str, range(1, n+1)))
        res = []
        while Q:
            for _ in range(k-1):
                Q.append(Q.popleft())
            res.append(Q.popleft())
        
        print("<"+ ', '.join(res) + ">")


if __name__ == "__main__":
    s = Solution()
    s.answer()