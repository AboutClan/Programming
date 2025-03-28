# 9012: 괄호
import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        for _ in range(int(input())):
            arr = list(input().strip())
            stack = []
            for a in arr:
                if a == ')':
                    try:
                        stack.pop()
                    except: # stack이 비어 있는 경우 = 시작이 ) 인 경우
                        print("NO")
                        break
                else: # ( 일 때는 stack에 삽입
                    stack.append(a)
            else: # for-else
                print("NO" if stack else "YES")

if __name__ == "__main__":
    s = Solution()
    s.answer()