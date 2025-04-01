stack = []        # 스택 저장 리스트
result = []       # 결과 저장 리스트

n = int(input())  # 첫째 줄에 명령의 수 N이 주어진다

for i in range(n):        # 둘째 줄부터 N개 줄에 명령이 주어진다 
    command = input()     # 명령 하나씩

    if command[0] == '1':    
        parts = command.split()  
        x = int(parts[1])         
        stack.append(x)       

    elif command == '2':    
        if len(stack) == 0:  
            result.append(-1)
        else:
            last = stack[len(stack)-1]  
            result.append(last)      
            del stack[len(stack)-1]     

    elif command == '3':    
        result.append(len(stack))

    elif command == '4':   
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)

    elif command == '5':    
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1]) 

for value in result:
    print(value)
