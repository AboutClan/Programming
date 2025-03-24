N = int(input()) 
card = list(map(int, input().split()))  

M = int(input())  
check = list(map(int, input().split()))  

for num in check:
    if num in card:
        print(1, end=' ')
    else:
        print(0, end=' ')

