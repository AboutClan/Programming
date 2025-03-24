N = int(input())
list1 = set(map(int,input().split()))
M =int(input())
list2 = list(map(int,input().split()))
result =[]
for i in range(len(list2)):
    if list2[i] in list1:
        result.append(1)
    else:
        result.append(0)
print(*result)