import sys

input = sys.stdin.readline

crd_cnt = int(input())
card_list = list(map(int, input().split()))

num = int(input())
num_list = list(map(int, input().split()))

card_list.sort()


def binary_search(num):
    start = 0
    end = crd_cnt - 1
    while start <= end:
        now = (end + start) // 2

        if card_list[now] == num:
            return 1
        if card_list[now] > num:
            end = now - 1
        else:
            start = now + 1
    return 0


for a in num_list:
    print(binary_search(a), end=" ")
