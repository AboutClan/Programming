arr_x = []
arr_y = []
for _ in range(3):
    x, y = map(int, input().split())
    if x in arr_x:
        arr_x.remove(x)
    else:
        arr_x.append(x)
    
    if y in arr_y:
        arr_y.remove(y)
    else:
        arr_y.append(y)

print(arr_x[0], arr_y[0])