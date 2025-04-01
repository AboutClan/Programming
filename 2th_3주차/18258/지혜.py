queue = []

result = []

n = int(input())

for i in range(n):
    command = input() 

    # 만약 명령이 "push X"라면
    if command.startswith("push"):
        parts = command.split()    
        x = int(parts[1])            
        queue.append(x)        

    elif command == "pop":
        if len(queue) == 0:         
            result.append(-1)
        else:
            result.append(queue[0])  
            del queue[0]           

    elif command == "size":
        result.append(len(queue))    

    elif command == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)

    elif command == "front":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])  

    elif command == "back":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[-1]) 

for value in result:
    print(value)
